![alt text](./logo_rsview_small.png) 

## Visualize RSV global distribution and disease severity

Authors: Kate Dusenbury, Katie Kistler, Jilliane Bruffey

Project for CSE 583. 


## Background 

Respiratory syncytial virus (RSV) is a common respiratory virus that, in healthy adults, usually causes an illness similar to the common cold. However, in infants and the elderly, RSV infection can cause severe disease. RSV is the leading cause of pneumonia in infants less than one year of age and is a leading cause of hospitalization due to acute respiratory tract infections in both infants and young children. 

Similar to other respiratory viruses, such as influenza, RSV circulates globally and with distinct seasonality. RSV generally circulates in the winter months in temperate climates and during the monsoon season in the tropics. Additionally, RSV has two distinct subtypes - A and B - and several genotypes. In any given location, it is generally thought that a single subtype will dominate the RSV season and that the dominant subtype cycles overtime with RSV A seasons giving way to RSV B seasons and vice versa. Furthermore, within each subtype, RSV genotypes appear to replace each other over time. Whether this evolution is due to selection from immune pressure or genetic drift is not fully understood, but RSV does appear to have a distinct pattern of infection over space and time, at least at the local level. A larger analysis of RSV sequencing data to look at patterns of subtype cycling and genotype replacement at a global level is lacking and would be an important resource to better understand the evolution and overarching dynamics of this important respiratory virus. 

Furthermore, it is known that for some respiratory viruses, such as rhinovirus, different subtypes or genotypes have different clinical severities. As such, we aim to examine if the subtype and genotype of RSV circulating in a particular location correlates with disease severity as determined by the number of children under 5 years old that die due to acute respiratory tract infection (ARTI). We realize that using deaths due to ARTI in children under 5 is an imperfect estimate of RSV disease burden, but believe this to be an appropriate surrogate due to the high RSV disease burden in this age group. Any large effects of genotype on disease severity should be noticeable with this coarse grain analysis.

Together our project, `RSView`, will provide an important resource for better understanding the global circulation dynamics of RSV and investigating the effects of genotype on disease severity. We recognize that this is very much a "first-pass" analysis, but believe these analyses and, especially, this framework for examining RSV (which is modeled off of the nextstrain.org platform developed by Trevor Bedford and Richard Neher) could prove quite useful for the field.

## Organization 




## Installation

To install and run `RSView` perform the following steps:

* clone the repo: git clone https://github.com/khdusenbury/viralseq_mapping.git

* create and activate the conda environment in the `environment.yml`:
    * `conda env create -f environment.yml`
    * `source activate rsview`

* install `RSView` by running `python setup.py install` within the cloned `viralseq_mapping` directory

Modules can then be run based on user needs.

To replicate our analyses:

* run `seq_download.py` with `--query 'human respiratory syncytial virus G'`

* run `genotype.py` 

* run `map_rsv.py` and/or `plot_rsv.py` with appropriate arguments.

