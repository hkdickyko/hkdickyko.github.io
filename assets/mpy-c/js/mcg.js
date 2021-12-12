// Get number of inputs required, return null if invalid input
function parseNumInputs() {
    const MAX_INPUTS = 10;
    var numInputs = parseInt($("#numInputs").val());
    if (numInputs == NaN) {
        $("#codeOutput").text("ERROR: Invalid number of inputs");
        numInputs = null;
    } else if (numInputs > MAX_INPUTS) {
        $("#codeOutput").text("ERROR: Too many inputs, maximum is " + MAX_INPUTS);
        numInputs = null;
    }

    return numInputs;
}

// Creates the inputs for setting input parameters
function generateInputOptions() {
    $(".inputsArea").empty();
    var numInputs = parseNumInputs();
    if (numInputs == null) return false;

    htmlStr = '';
    for (var inputVal = 0; inputVal < numInputs; inputVal++) {
        if (inputVal % 2 == 0) {
            htmlStr += '<div class="u-full-width">';
        }
        htmlStr += '<div class="three columns">';
        htmlStr += '<label for="outputType">輸入 ' + (inputVal + 1) + ' 類型</label>';
        htmlStr += '<select class="u-full-width" id="inputType' + (inputVal + 1) + '" oninput="generateCode">';
        htmlStr += '<option value="bool">Boolean</option>';
        htmlStr += '<option value="int">Integer</option>';
        htmlStr += '<option value="float">Float</option>';
        htmlStr += '<option value="stringnull">String, null terminated</option>';
        htmlStr += '<option value="stringlen">String, with length</option>';
        htmlStr += '<option value="list">List / Tuple</option>';
        // htmlStr += '<option value="dict">Dictionary</option>';
        htmlStr += '</select>';
        htmlStr += '</div>';
        htmlStr += '<div class="three columns">';
        htmlStr += '<label for="outputName">輸入 ' + (inputVal + 1) + ' 名稱</label>';
        htmlStr += '<input class="u-full-width" type="text" id="inputName' + (inputVal + 1) + '" value="arg_' + (inputVal + 1) + '" oninput="generateCode" />';
        htmlStr += '</div>';
        if (inputVal % 2 == 1 || inputVal + 1 == numInputs) {
            htmlStr += '</div>';
        }
    }
    $(".inputsArea").append(htmlStr);
    $(".input-form input, .input-form select").each(function(index) {
        $(this).on('input', generateCode);
    });
}

// Copies the code box contents to clipboard
function copyCode() {
    var copyText = document.getElementById("_hiddenCopyText_");
    copyText.select();
    document.execCommand("copy");
}

// Verifies whether an argument name is valid C
// Returns a string if an error found, otherwise returns null
function checkArgName(nameStr) {
    if (nameStr.length == 0) return "Name cannot be empty";
    else if (nameStr.length > 99) return "Name too long";
    else if (!/^[a-z_][a-z0-9_]*$/i.test(nameStr)) {
        return "Name either starts with a number or has an invalid character";
    }

    return null;
}

// Retrieves a dictionary of all of the input parameters
// Returns null if invalid data found
function getFormDict() {
    var outDict = {};
    var valid;

    // Get function name
    outDict['function'] = $('#functionName')[0].value;
    valid = checkArgName(outDict['function']);
    if (valid != null) {
        $("#codeOutput").text("ERROR: Function name - " + valid);
        return null;
    }

    // Get output data
    outDict['output'] = {
        'name': $('#outputName')[0].value,
        'type': $('#outputType')[0].value
    }
    valid = checkArgName(outDict['output']['name']);
    if (valid != null) {
        $("#codeOutput").text("ERROR: Output name - " + valid);
        return null;
    }

    // Get input data
    outDict['inputs'] = []
    var numInputs = parseNumInputs();
    if (numInputs == null) return null;
    for (var inputVal = 0; inputVal < numInputs; inputVal++) {
        var inputDict = {
            'name': $('#inputName' + (inputVal + 1))[0].value,
            'type': $('#inputType' + (inputVal + 1))[0].value
        }
        valid = checkArgName(inputDict['name']);
        if (valid != null) {
            $("#codeOutput").text("ERROR: Input name " + (inputVal + 1) + " - " + valid);
            return null;
        }
        outDict['inputs'].push(inputDict);
    }

    return outDict;
}

// Function that generates the output code, and puts it in the relevant textbox
function generateCode() {
    // Setup
    const INDENT = '    ';
    const MAX_DISCRETE_ARGS = 3;
    var formDict = getFormDict();
    if (formDict == null) return;

    outputCode = '// MicroPython 應用程序接口的頭文件\n';
    outputCode += '#include "py/obj.h"\n';
    outputCode += '#include "py/dynruntime.h"\n';
    outputCode += '\n';

    // Create function initialiser
    outputCode += '// 函數定義開始 ----------------------\n';
    outputCode += 'STATIC mp_obj_t ' + formDict['function'] + '(';
    var numInputs = formDict['inputs'].length;
    if (numInputs <= MAX_DISCRETE_ARGS) {
        for (var index = 0; index < formDict['inputs'].length; index++) {
            if (index == 0) {
                outputCode += '\n';
            }
            outputCode += INDENT + INDENT;
            outputCode += 'mp_obj_t ' + formDict['inputs'][index]['name'] + '_obj';
            if (index + 1 != formDict['inputs'].length) {
                outputCode += ',\n';
            }
        }
    } else {
        outputCode += 'size_t n_args, const mp_obj_t *args';
    }
    outputCode += ') {\n';

    // Cast input arguments to appropriate types
    for (var index = 0; index < formDict['inputs'].length; index++) {
        var argName;
        if (numInputs <= MAX_DISCRETE_ARGS) {
            argName = formDict['inputs'][index]['name'];
        } else {
            argName = 'args[' + index + ']';
        }

        var mpType, mpObjGet;
        switch (formDict['inputs'][index]['type']) {
            case 'bool':
                mpType = 'bool';
                mpObjGet = 'mp_obj_is_true';
                break;
            case 'int':
                mpType = 'mp_int_t';
                mpObjGet = 'mp_obj_get_int';
                break;
            case 'float':
                mpType = 'mp_float_t';
                mpObjGet = 'mp_obj_get_float';
                break;
            case 'stringnull':
                mpType = 'const char*';
                mpObjGet = 'mp_obj_str_get_str';
                break;
            case 'stringlen':
                mpType = 'const char*';
                mpObjGet = 'mp_obj_str_get_data';
                break;
            case 'list':
                mpType = null;
                mpObjGet = INDENT + 'mp_obj_t *' + argName + ' = NULL;\n';
                mpObjGet += INDENT + 'size_t ' + argName + '_len = 0;\n';
                mpObjGet += INDENT + 'mp_obj_get_array(' + argName + '_obj, &' + argName + '_len, &' + argName + ');\n';
                mpObjGet += INDENT + 'mp_int_t ' + argName + '_item_1 = mp_obj_get_int(' + argName + '[0]);\n';
                mpObjGet += INDENT + 'mp_float_t ' + argName + '_item_2 = mp_obj_get_float(' + argName + '[1]);\n';
                mpObjGet += INDENT + 'const char* ' + argName + '_item_3 = mp_obj_str_get_str(' + argName + '[2]);\n';
                if (index + 1 < formDict['inputs'].length) {
                    mpObjGet += '\n';
                }
                break;
            default:
                mpType = 'mp_TODO_t';
                mpObjGet = 'mp_obj_get_TODO';
        }

        if (mpType == null) {
            outputCode += mpObjGet;
        } else if (formDict['inputs'][index]['type'] == 'stringlen') {
            outputCode += INDENT + 'size_t ' + argName + '_len;\n';
            outputCode += INDENT + mpType + ' ' + formDict['inputs'][index]['name'] + ' = ';
            outputCode += mpObjGet + '(' + argName + '_obj, &' + argName + '_len);\n';
        } else {
            outputCode += INDENT + mpType + ' ' + formDict['inputs'][index]['name'] + ' = ';
            outputCode += mpObjGet + '(' + argName + '_obj);\n';
        }
    }

    // Manage return
    var retType = '';
    var retCode = '';
    switch (formDict['output']['type']) {
        case 'void':
            retCode = INDENT + ' return mp_const_none;\n';
            break;
        case 'bool':
            retType = 'bool';
            retCode += INDENT + formDict['output']['name'] + ' = true;\n'
            retCode += INDENT + 'return mp_obj_new_bool(' + formDict['output']['name'] + ');\n'
            break;
        case 'int':
            retType = 'mp_int_t';
            retCode += INDENT + formDict['output']['name'] + ' = 99;\n'
            retCode += INDENT + 'return mp_obj_new_int(' + formDict['output']['name'] + ');\n'
            break;
        case 'float':
            retType = 'mp_float_t';
            retCode += INDENT + formDict['output']['name'] + ' = (float)(9.87654 * 1.0);\n'
            retCode += INDENT + 'return mp_obj_new_float((float)(' + formDict['output']['name'] + '));\n'
            break;
        case 'string':
            retType = '';
            retCode = INDENT + '// 函數定義: mp_obj_t mp_obj_new_str(const char* data, size_t len); size_t = int;\n'
            retCode += INDENT + 'const char* data = "abcdef";\n'
            retCode += INDENT + 'int length = strlen(data);\n'
            retCode += INDENT + 'return mp_obj_new_str(data, length);\n'
                // retCode += INDENT + 'return mp_obj_new_str(<' + formDict['output']['name'] + '_ptr>, <' + formDict['output']['name'] + '_len>);\n'
            break;
        case 'bytes':
            retType = '';
            retCode = INDENT + '// 函數定義: mp_obj_t mp_obj_new_bytes(const byte* data, size_t len);\n'
            retCode += INDENT + 'byte bdata[] = { 0xFF, 0xF0, 0x0F, 0x11 };\n'
            retCode += INDENT + 'const byte* data = bdata;\n'
            retCode += INDENT + 'int length = sizeof(bdata);\n'
            retCode += INDENT + 'return mp_obj_new_bytes(data, length);\n'
                //retCode += INDENT + 'return mp_obj_new_bytes(<' + formDict['output']['name'] + '_ptr>, <' + formDict['output']['name'] + '_len>);\n'
            break;
        case 'tuple':
            retType = '';
            retCode = INDENT + '// 函數定義: mp_obj_t mp_obj_new_tuple(size_t n, const mp_obj_t *items);\n'
            retCode += INDENT + 'mp_obj_t ' + formDict['output']['name'] + '[] = {\n'
            retCode += INDENT + INDENT + 'mp_obj_new_int(123),\n'
            retCode += INDENT + INDENT + 'mp_obj_new_float((float)(456.789)),\n'
            retCode += INDENT + INDENT + 'mp_obj_new_str("hello", 5),\n'
            retCode += INDENT + '};\n'
            retCode += INDENT + 'return mp_obj_new_tuple(3, ' + formDict['output']['name'] + ');\n'
            break;
        case 'list':
            retType = '';
            retCode = INDENT + '// 函數定義: mp_obj_t mp_obj_new_list(size_t n, const mp_obj_t *items);\n'
            retCode += INDENT + 'mp_obj_t ' + formDict['output']['name'] + '[] = {\n'
            retCode += INDENT + INDENT + 'mp_obj_new_int(123),\n'
            retCode += INDENT + INDENT + 'mp_obj_new_float((float)(456.789)),\n'
            retCode += INDENT + INDENT + 'mp_obj_new_str("hello", 5),\n'
            retCode += INDENT + '};\n'
            retCode += INDENT + 'return mp_obj_new_list(3, ' + formDict['output']['name'] + ');\n'
            break;
        case 'dict':
            retType = '';
            retCode = INDENT + 'mp_obj_dict_t *' + formDict['output']['name'] + ' = mp_obj_new_dict(0);\n'
            retCode += INDENT + 'mp_obj_dict_store(' + formDict['output']['name'] + ', mp_obj_new_str("element1", 8), mp_obj_new_int(123));\n'
            retCode += INDENT + 'mp_obj_dict_store(' + formDict['output']['name'] + ', mp_obj_new_str("element2", 8), mp_obj_new_float((float)(456.789)));\n'
            retCode += INDENT + 'mp_obj_dict_store(' + formDict['output']['name'] + ', mp_obj_new_str("element3", 8), mp_obj_new_str("hello", 5));\n'
            retCode += INDENT + 'return ' + formDict['output']['name'] + ';\n'
            break;
        default:
            retType = 'mp_TODO_t';
            break;
    }
    if (retType != '') {
        outputCode += INDENT + retType + ' ' + formDict['output']['name'] + ';\n';
    }
    // User code section
    outputCode += INDENT + '// 代碼開始 ----------------------\n';
    outputCode += '\n\n';

    outputCode += INDENT + '// 代碼結束 ----------------------\n';
    if (retCode == '') {
        outputCode += INDENT + 'return ' + formDict['output']['name'] + ';\n';
    } else {
        outputCode += retCode;
    }

    outputCode += '}\n';
    outputCode += 'STATIC '
        // Function wrapper
    if (numInputs < 4) {
        outputCode += 'MP_DEFINE_CONST_FUN_OBJ_' + numInputs + '(' + formDict['function'] + '_obj, ' + formDict['function'] + ');\n';
    } else {
        outputCode += 'MP_DEFINE_CONST_FUN_OBJ_VAR_BETWEEN(';
        outputCode += formDict['function'] + '_obj, ' + numInputs + ', ' + numInputs + ', ' + formDict['function'] + ');\n';
    }
    outputCode += '// 函數定義結束 ----------------------\n';

    // Map table
    outputCode += '\n';
    outputCode += 'mp_obj_t mpy_init(mp_obj_fun_bc_t *self, size_t n_args, size_t n_kw, mp_obj_t *args)\n';
    outputCode += '{\n';
    outputCode += INDENT + 'MP_DYNRUNTIME_INIT_ENTRY \n';  
    outputCode += '\n';
    outputCode += '// 函數入口點定義開始 ----------------------\n';
    outputCode += INDENT + 'mp_store_global(MP_QSTR_' + formDict['function'] + ', MP_OBJ_FROM_PTR(&' + formDict['function'] + '_obj));\n';
    outputCode += '// 函數入口點定義結束 ----------------------\n';
    outputCode += '\n';
    outputCode += INDENT + 'MP_DYNRUNTIME_INIT_EXIT\n';
    outputCode += '}\n';

    $("#codeOutput").text(outputCode);

    // Add text to hidden element
    const targetId = "_hiddenCopyText_";
    var target = document.getElementById(targetId);
    if (!target) {
        target = document.createElement("textarea");
        target.style.position = "absolute";
        target.style.left = "-9999px";
        target.style.top = "0";
        target.id = targetId;
        document.body.appendChild(target);
    }
    target.textContent = outputCode;
}

// Code ran on page startup
$(document).ready(function() {
   $("#numInputs").on('input', generateInputOptions);
   $("#generateCode").click(function() {
       generateCode;
       $(window).scrollTo("#codeOutput", 800);
    });
   $("#copyCode").click(copyCode);
   $(".input-form input, .input-form select").each(function(index) {
       $(this).on('input', generateCode);
   });
   $("#showExamples").change('input', generateCode);
   generateCode();
});