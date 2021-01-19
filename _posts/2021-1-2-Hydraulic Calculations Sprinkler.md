---
category: 工程 
tags: [消防系統]
---


# Hydraulic Calculations - Sprinkler

## The pipe friction from the sprinkler rule

![](https://latex.codecogs.com/svg.latex?\Large&space;P_{p}=K_{p}\times{L}\times{Q}^{1.85})
  
## The pressure loss at sprinkler 

![](https://latex.codecogs.com/svg.latex?\Large&space;Q=K_{s}\times\sqrt{P_{s}})

 - Q<sub>?</sub> = flow rate in litres per second (l/s)
 - L<sub>?</sub> = Length including equivalent lenght for fitting (m)
 - P<sub>p?</sub> = loss of pressure in pipe in bars
 - P<sub>s?</sub> = loss of pressure in sprinkler in bars
 - P<sub>z?</sub> = static difference between sprinkler in bars
 - K<sub>p?</sub> = constant depending on the size and type of the pipe
 - K<sub>s</sub> = constant depending on the orifice size of the sprinkler head
  
「?」is number for reference。


## Find the location for calculation

### Hydraulically most favourable location

 - The pressure loss is minimum so the flow rate is maximum.

### Hydraulically most unfavourable location

 - The flow rate is minimum so the pressure loss is maximum.

## Calculation method

1. Check number of sprinklers are necessary to calculate in hydraulically most unfavourable location.
   - Sprinkers in the Area of operation
  
2. Find the flow rate of the most remote sprinkler
   - Q<sub>0</sub> = design density x area per sprinkler
 
3. Check the minimum pressure of the most remote sprinker
   
    ![](https://latex.codecogs.com/svg.latex?\Large&space;P_{s}=\left(\frac{Q_{0}}{K_{s}}\right)^{2})

4. Calculate the pipe loss connected to the sprinkler

    ![](https://latex.codecogs.com/svg.latex?\Large&space;P_{p}=K_{p}\times{L_{0}}\times{Q_{0}}^{1.85})

5. The pressure of the next sprinkler 

    ![](https://latex.codecogs.com/svg.latex?\Large&space;\Large&space;P_{s1}=P_{s}+P_{p}+P_{z})
   
6. To calculate the flow of the next sprinkler

    ![](https://latex.codecogs.com/svg.latex?\Large&space;Q_{1}=K_{s}\times\sqrt{P_{s1}})

7. To calculate the pipe loss of the next pipe

    ![](https://latex.codecogs.com/svg.latex?\Large&space;P_{p1}=K_{p1}\times{L_{1}}\times{Q_{1}}^{1.85})

8. For the whole range pipe treat it as a open outlet to find the K

    ![](https://latex.codecogs.com/svg.latex?\Large&space;K=\frac{Q}{\sqrt{P}})

9. For the other whole range pipe with less pipe loss, you may use the same procedure as 3 to 8 to find the K<sub>E</sub> equivalent 

    ![](https://latex.codecogs.com/svg.latex?\Large&space;Q_{actual}=K_{E}\times\sqrt{P_{actual}})

    - Q<sub>actual</sub> was calculated from the most remote sprinkler



