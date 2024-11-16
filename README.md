# Hybrid Modeling Tutorial
Hybrid Modeling is a modeling technique in which a physics-based model is combined with a data-based approach. 
By combining the best of both worlds, we trade off the benefit of prior knowledge when training data is scarce with the flexibility of a data-driven approaches when training data is abundant. 
In this notebook we demonstrate the power of hybrid modeling by modeling data, which roughly follows the amplitude of a non-linearly damped oscillator with missing data.

The paper [Hybrid Modeling Design Patterns (Maja Rudolph, Stefan Kurz, Barbara Rakitsch)](https://link.springer.com/article/10.1186/s13362-024-00141-0) provides additional context and background to this notebook, as well as a broader perspective on the topic.

# Purpose of the Project
This software is a tutorial, solely developed for educational
purpose. It will neither be maintained nor monitored in any way.

# Installation Guidelines
First create a [conda](https://anaconda.org/anaconda/conda) environment

    conda create -n HYM_notebook python=3.11

Activate the environment

    conda activate HYM_notebook

Install packages from requirements file using conda

    pip install -r requirements.txt

# Trouble Shooting
If you have problems, importing the packages in Jupyter, add your Conda environment to Jupyter as a new kernel.

    python -m ipykernel install --user --name=HYM_notebook --display-name "HYM notebook"

Open Jupyter, go to Kernel > Change Kernel and select "HYM notebook".


# License
Benchmarks is open-sourced under the MIT license. See the
[LICENSE](LICENSE) file for details.
