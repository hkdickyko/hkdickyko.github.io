---
category: 工程 
tags: [消防系統]
---


# Hydraulic Calculations - Sprinkler

## The pipe friction from the sprinkler rule

![](https://latex.codecogs.com/svg.latex?\Large&space;P_{p}=K_{p}\times{L}\times{Q}^{1.85})
  
## The pressure loss at sprinkler 

![](https://latex.codecogs.com/svg.latex?\Large&space;Q=K_{s}\times\sqrt{P_{s}})

 - Q<sub>?</sub> = flow rate in litres per second (l/s)，「?」is number for reference。
 - L<sub>?</sub> = Length including equivalent lenght for fitting (m)，「?」is number for reference。
 - P<sub>p?</sub> = loss of pressure in pipe in bars per meter。
 - P<sub>s?</sub> = loss of pressure in sprinkler in bars per meter。
 - K<sub>p?</sub> = constant depending on the size and type of the pipe。
 - K<sub>s?</sub> = constant depending on the orifice size of the sprinkler head。

## Find the location for calculation

### Hydraulically most favourable location

 - The pressure loss is minimum so the flow rate is maximum.

### Hydraulically most unfavourable location

 - The flow rate is minimum so the pressure loss is maximum.

## Calculation method

1. Check number of sprinklers are necessary to calculate.
   - Sprinkers in the Area of operation
  
2. Find the flow rate of the most remote sprinkler
   - Q<sub>0</sub> = design density x area per sprinkler
 
3. Check the minimum pressure of the most remote sprinker
   
    ![](https://latex.codecogs.com/svg.latex?P_{s}=\left(\frac{Q_{0}}{K_{s}}\right)^{2})

4. Calculate the pipe loss connected to the sprinkler

    ![](https://latex.codecogs.com/svg.latex?P_{p}=K_{p}\times{L}\times{Q_{0}}^{1.85})

5. The pressure of the next sprinkler

    ![](https://latex.codecogs.com/svg.latex?P_{s1}=P_{s}+P_{p})
   
6. To calculate the flow of the next sprinkler

    ![](https://latex.codecogs.com/svg.latex?Q_{1}=K_{s}\times\sqrt{P_{s1}})

7. To calculate the flow of the next pipe    

    ![](https://latex.codecogs.com/svg.latex?P_{p1}=K_{p1}\times{L}\times{Q_{1}}^{1.85})
