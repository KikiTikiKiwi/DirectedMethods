# Theory

## Mechanisms of Research Group's Sodium Borate Glass
- The parent glass is made with a composition of $Na_2O_2B_2O_3# and doped with varying amounts of Cerium Oxide - 0.01 to 0.05 mol%. Other glasses are composed of borax, then held at 1110,1200, and 1300 celcius for 1,2 or 3 hours. They make up most of the collected data containing 0.05 mol% of cerium-oxide.
- Thermal analysis for the parent and borate glass was done by looking at the specific heat capacity of the samples. They are heated to 900 c at a rate of 20 c per minute. As the heat flows into the sample, this is done so against the temperature. By doing this, glass transitions are observed for the samples. It is observed then that the crystallization temperatures increase for samples doped with higher cerium oxide. The Hruby parameter increases as the amounts of Cerium oxide increase, suggesting that an elevated amount of Cerium-Oxidemakes the glass durable agaisnt crystallization. The group's FTIR spectroscopy analysis has confirmed modifications of the glass network {cite}`nano12142363`. So as we modify the glass network with more elevated Cerium Oxide amounts, producing greater oxidization to reduced 'status', we are changing the glass network itself. It seems to me the more we 'ALLOW' for oxidization to occur, then, of course, we will have an elevated Ce3+ concentration. NEEDS REVISING, doesnt sound right
## Cerium Oxidation: Condensed Matter Lens
- We may attribute the potentials to an atom's number of protons and electrons. We can imagine around this particular atom; it has a complex approximation of a "finite well" with an electron finding itself in a bound state. Now, what about structures, not only  atoms by themselve, but atoms arranged and bonded in a particular way? Different structures, made up of the same compositions, will have different potential energies, which means our bound states will differ from other species of the same composition. This idea closely models differnet oxidization states within a sample, as a result of different oxidization states, XAFS spectrums will vary from one another.

### Concept of XANES
- We can think of XANES in terms of Beer Lambert's Law, where the x-ray's Absorption is proportional to the distance that the x-rays have to travel through and the concentration of the sample. 

- If we now designate the number of photons absorbed in a given material, is equivalent to the intensity before entering and the thickness of an infintismal value, we arrive at the following relation for slight decreases in light intensity.

$$
dI = a I dx
$$

- Which when integrated becomes...

$$
 ln(I) = ax + c
$$

- Now, we have mentioned slight changes in lights intensity for infintisimal lenghts of a material, but what about absorbance? We know it has to be porportional to the concentration of the material, giving this relation...

$$
    \frac{-dI}{dx} \alpha c
$$

- Combining the two laws, we say then absorbance is equivalent to the path of the photons, their energy, and concentration of the sample.

$$
    \frac{-dI}{dx} = b c I
$$

$$
    I = I_0 \exp{-bcx}
$$

- The absorbtion coefficent then becomes b times c, meaning the absorbtion coefficent is dependant on the concentration and some constant of porportionality dependant on the material. But as we vary the energy of the photons while keeping the concentration constant, the absoprtion will change as the energy increases, making it a function of energy.

### Working With Mass Absorption Coefficient 
- Basically we determined above that the packing density of the sample will affect the amount of atoms in a given thickness. As a result it is easier to work with the mass absorption coefficient.

$$
    U_m(E) = \frac{U(E)}{\rho}
$$

- But some working samples do not have known Mass Absorption values, so its up to the person to decide whats best and try to replicate every experiment as perfectly as possible. Yet again, there is a way around this by converting powdered substances thickness into mass Measurements.

### Powdered Spreads
- We measure the area over which the layer of powder is spread and convert the thickness into a mass.

$$
    U_m(E)\rho x = U_m \frac{m}{V} x = U_m \frac{m}{Ax} x = \frac{U_m m}{A}
$$

- This works great for us! As we do not need to know the density of our material.
- And because we may work with samples with varying compositions as a result of slight changes in each of their creations, this is a better way to help us because mass and area are very easy to obtain {cite}`XAFS`.

### XANES for CNPs
- X-ray absorption near edge structure spectrooscopy (XANES) is used to observe oxidization states of cerium ions in CNP. In a XANES spectra for CNP there are four observed peaks of varying amplitudes depending on the ratios of the oxidized states $Ce^{3+}/Ce^{4+}$ in the L-3 edge ~ Ref fig {numref}`markdown-peaks`. Both A and B  correlate to the $Ce^{4+}$ peak while C correlates to the $Ce^{3+}$ peak {cite}`ZHANG200474`. As the $Ce^{3+}$ concentration goes up, peak C will also increase until its a pure sample. Anything between that of a pure $Ce^{4+}$ and $Ce^{3+}$ sample will take on peaks of different hights. But there are constraints to which peaks will increase and decrease for varying concentrations, ~ Ref fig {numref}`markdown-spectra`. In this figure we observe that for pure $Ce^{3+}$ peak C is at its max while peak B has vanished almost entirly. This is because peak B is a forbidden state in $Ce_2O_3$. 

:::{figure-md} markdown-peaks
<img src="Peaks.png" alt="XANES Peaks" class="bg-primary mb-1" width="300px">

{cite}`ZHANG200474`
:::

:::{figure-md} markdown-spectra
<img src="XANES.png" alt="XANES Spectrum" class="bg-primary mb-1" width="300px">

This is a caption in **Markdown**!
:::

Dipping back into the condensed matter lens, we look at the overall net superposition of all species, but in XANES, the individiual species can not be seperated, we just observe the overlap of these specie's spectra being produced by different combinations of oxidation and reduction. 


## Linear Combination Fitting
- There is still the problem of determining the ratios for CNP samples. In order to determine the ratio of the two oxidized states, analysis must be performed using reference samples to the measured data. The spectrum samples that are being compared to the data are also known as a standard. Thus, the idea of Linear Combination Fitting can simply be put as the following - Its the idea that an unknown spectra can be explained by a combination of standards to best match the composition of the unkown spectra. LCF can be used then to find the relative amounts of the known standards in the CNP samples {cite}`XAFS`.

## Deglitching
- We define glitches as sharp deviations in the measured absorption. Small glitches can be removed by fourier filtering.
- Very large glitches can affect our normalization and background subtraction. Thus large gltiches should be taken care of for the sake of reliable data.
- Methods include removing that point or better yet, interpolating that data,
- This however only works if we oversamples our data in the energy space.
## Flatten/Normalize Data
- Analysis depends heavily on comparing our spectra of samples. Some of which are 'dissimilar in fine structure'. More will be mentioned on this later.