# projet-ML-DL

In this readme we'll only cover what is necessary to run the file present under **/data_analysis/Data_Analysis.ipynb**
since this is actually the whole project.

We chose to keep the name "data analysis" because this project was done more in a way to understand how to approach a *Machine Learning* and/or *Deep Learning* problem than trying to have great result henceforth the name "data analysis". 
##  Pre-Requisite

For this project only there's two pre requisite :
- [Python](https://www.python.org/downloads/)
- [Anaconda](https://docs.anaconda.com/anaconda/install/) or [Miniconda](https://docs.anaconda.com/miniconda/install/)

We'll use miniconda (or anaconda) to create our virtual environnement. 

## Setup

**TL;DR**

Run those command : 
```bash
conda env create -f env.yml

conda activate projet-math

.\pull_dataset.sh

jupyter notebook
```


**Step-by-step**

First we want to create our virtual environment conda and the *env.yml* file are here to help with that, open a terminal and type :
```bash
conda env create -f env.yml
```

this will tell conda to create a new virtual environment with all dependencies listed in the file.Once this command is run type :
```bash
conda env list
```
You should see your env **"projet-maht"**, activate it by running :
```bash
conda activate projet-math
```
Then you'll need to pull the dataset from kaggle to do it, just run the bash script (in your terminal or with git bash):
```bash
.\pull_dataset.sh
```
Let yourself be guided by the script once this is done you should see in dataset folder a new file called : **"dataset.csv"**

**/!\ If for any reason you can't get the dataset this way you can download it manually [here](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset), just don't forget, once downloaded, to put it in the dataset folder.  /!\\**

## Run

Then once everything is set-up you have two possibilities for running this project : jupyter notebook webinterface or use an extension in you IDE that let you access and use jupyter notebook.

**Jupyter-notebook webinterface**

For this solution just open a terminal (preferably in this project) and type
```bash
jupyter notebook
```
This will launch the jupyter server then you can go to **Data-Analysis.ipnyb** and you're good to go !

**Jupyter-notebook IDE extension**

Since I'm using VSCode you can find the appropriate extension [here](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter). (Or fo to the extension pannel and type "jupyter")

Then you can directly go to the file and run each code block as you wish.

## Remove conda environment

Once you finished don't forget to deactivate your conda environment and remove it if you've got no use for it anymore !

```bash
conda deactivate
```

and then 

```bash
conda remove --name projet-math
```

if your want to be sure that the conda environment is correctly removed : 

```bash
conda info --envs
```
## Contact

We now we made mistakes and there's always place for improvement so feel free to contact us :

 - Jean Roelens - jean.roelens@ynov.com    
 - Raphael Duran - raphael.durand@ynov.com

