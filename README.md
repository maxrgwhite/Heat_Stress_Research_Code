Hello. This code lets you compare Lu and Romps' (2022) Heat Index algorithm to others' (named in the notebooks. Lu and Romps' (2022) algorithm is available in Python, R, and Fortran code at https://romps.berkeley.edu/papers/pubs-2020-heatindex.html#:~:text=To%20extend%20the%20heat%20index,observable%20measure%20of%20physiological%20stress.

To run the code, you will need some spatial data. I used ERA5-Land data at the hourly level for the Limpopo province of South Africa. This data can be acquired using step 1 below.

The following files need to be executed in order. 

- Step 1: Open the *data_requests* file and choose to download either ERA5 or ERA5–Land data
  - You will need a Copernicus (CDS) account and to specify your CDS API Key. See the following link for a tutorial: https://ecmwf-projects.github.io/copernicus-training-c3s/cds-tutorial.html
  - You can easily find the coordinate bounds using this helpful tool: https://boundingbox.klokantech.com/.
- Step 2: Open _basic_info.py_ and change the file paths in there
  - As you run each file below, you will notice that more files are added to _basic_info.py_. This was set to prevent you from having to repeatedly type in the filepaths you need each time you open a new file.
- Step 3: Run _creating_and_concatenating_cubes.ipynb_
  - Creates Iris "cubes" from the individually requested files from Step 1.
- Step 4: Run _cube_creation_frontend.ipynb_
  - Creates further files from the step 3 file required for further analyses
- Step 5: Run _algorithm_comparison_tables.ipynb_
  - Creates plots for the difference in heat indices for each temperature-humidity pairing per heat index algorithm relative to Lu and Romps' (2022) algorithm 
- Step 6: Run _algorithm_22_Processing.ipynb_
  - Creates the Lu and Romps (2022) cube
- Step 7: Run _data_analysis_frontend.ipynb_
  - Creates spatial plots and time series plots
- Step 8: Run _calculating_scaling_factor.ipynb_
  - Creates a 'scaling factor' to be used in step 9. This is necessary to create as the maximum daily heat indices are estimated with daily maximum air temperature and minimum relative humidity, while available projections only allow the creation of mean daily heat indices (a function of daily mean air temperature and mean relative humidity).
- Step 9: Run _projections.ipynb_ after changing the filepaths to suit you.

**Useful tips**
Don't worry about the equivalent "backend" files unless you'd like to make some changes to the outputs
The code is split into many files to prevent crashing regardless of device capabilities. If files still crash, batch process data by extracting subsets of the cubes and then concatenating them. See step 6's code for an example of how to do this.
