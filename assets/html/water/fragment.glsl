uniform sampler2D Matcap;      varying vec2 Point;
    void main(void){
    // texture2D() 获取颜色值
    vec4 color = texture2D(Matcap, Point);
    gl_FragColor = color;
    }