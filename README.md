# GeoPipeline-StarterKit

## Description

A walkthrough on retrieving datasets from [NASA Earthdata](https://urs.earthdata.nasa.gov/home), as well as a template to create machine learning models that use precipitation data in the vicinity of hydroelectric dams to predict resevoir levels.

## Modules Used

- `notebook`: Jupyter Notebooks provides an interactive environment for your data processing and visualization tasks.
- `pandas`: A powerful Python data analysis toolkit, ideal for data manipulation and cleaning.
- `rasterio`: Handles raster data (like satellite imagery) in Python, making it a crucial tool for geospatial data processing.
- `requests`: A simple, yet powerful, HTTP library for Python, used for making API calls (such as to retrieve data from NASA Earthdata).

## Device Requirements

- This project was completed on MacOS, and some of the scripts (ex. `download-earthdata-from-urls-file.sh`) assume use on a MacOS/Linux system (ex. the use of `curl` vs. `wget`). Some minor modifications will be required to run all steps on a Windows device.
- The dataset specified in the walkthrough / example will require approximately ~660 MB of disk space.

## Getting Started

### 1. Retrieve hydroelectric dam data

#### Retrieve dam coordinates

This is necessary as a first step to narrow down the coordinates for the following step of percipitation data retrieval.

For this demonstration, a list of BC Hydro dams and their respective coordinates, capacities and year of construction has been retrieved from Wikipedia (see [List of generating stations in British Columbia](https://en.wikipedia.org/wiki/List_of_generating_stations_in_British_Columbia)).

This data has been manually transformed into a CSV (see [BC Hydro dams as of 2024-01-01](./input/bc-hydro-dam-coordinates/bc-hydro-dams-as-of-2024-01-01.csv)).

#### Determine coordinates (bounding box) for the dataset

See the [dam-coordinates notebook](./notebooks/dam-coordinates.ipynb) to define a buffer size (in kms) around the outermost dams. The output of this notebook will provide an input for data retrieval when selecting precipitation data.

Example output for the [BC Hydro dams as of 2024-01-01](./input/bc-hydro-dam-coordinates/bc-hydro-dams-as-of-2024-01-01.csv) with a 100 km buffer size:

```
[-131.206, 47.576, -113.633, 56.917]
```

#### Retrieve hydroelectric resevoir levels

TBA

### 2. NASA Earthdata account setup

#### Create your NASA Earthdata account

See [here](https://disc.gsfc.nasa.gov/data-access).

#### Link your account with GES DISC

1. See [here](https://disc.gsfc.nasa.gov/earthdata-login).
2. Verify `NASA GESDISC DATA ARCHIVE` is listed in your [Earthdata Authorized Apps](https://urs.earthdata.nasa.gov/users/jonathanearthdata/authorized_apps) page.

### 3. Choose appropriate Earthdata dataset

#### Define the desired characteristics of the dataset

The hope was to find a Global Precipitation Management Integrated Multi-satellitE Retrievals (GPM IMERG) dataset with these characteristics:

- Data Latency: Late
- Spatial Resolution: L3
- Temporal Resolution: 1 Day

#### Select an dataset based on the desired characteristics

Use the [Goddard Earth Sciences Data and Information Services Center (GES DISC) data collections search](https://disc.gsfc.nasa.gov/) to find an appropriate dataset.

The Earthdata (GES DISC) precipitation dataset idenfied as suitable for this repository based on the above characteristics is:

- **GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V06 (`GPM_3IMERGDL`)**
  - [Summary](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_06/summary)
  - [README](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/doc/README.GPM.pdf)

### 4. Downloading the Earthdata dataset

Since the aforementioned dataset is not checked into this repository, you will need to download it yourself by performing the following steps:

#### Setup Earthdata prerequisite files

- Follow the instructions at: [GES DISC - How to Generate Earthdata Prerequisite Files](https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Generate%20Earthdata%20Prerequisite%20Files)

#### Fill in the download form

Select an appropriate date range, coordinates (as defined in a [previous section](#determine-coordinates-bounding-box-for-the-dataset)), and variables in the Earthdata download form. It is recommended to select all variables, if you are not immediately sure which are appropriate - they can then be omitted from the selected features later on if they are unneeded.

#### Download the Earthdata URLs

Once the form has valid values selected, a set of URLs will be generated as a downloadable text file, which will be utilized in one of the following steps to download all appropriate files in the dataset.

The precipitation dataset used in this example has its URL file saved [here](./input/earthdata-ges-disc/urls/subset_GPM_3IMERGDL_06_20240101_212853_.txt).

#### Download the Earthdata dataset (official documentation)

Once the prerequisite files have been set up, and the URLs file has been downloaded, it is recommended that you review the official instructions on using `wget` or `curl` to download all URLs in the previously downloaded URLs text file:

- [GES DISC - How to Access GES DISC Data Using wget and curl](https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Access%20GES%20DISC%20Data%20Using%20wget%20and%20curl)

#### Download the Earthdata dataset (streamlined approach)

Alternatively, [a script that uses `curl`](./download-earthdata-from-urls-file.sh) has been created to streamline this process, allowing easy selection of the URLs file and the output directory for all files that will be downloaded.

Review the script, ensuring the `urls_file` and `output_dir` variables are set as desired. Then, run it:

```sh
./download-earthdata-from-urls-file.sh
```

By default, the downloaded files will be saved to the the target path: [input/earthdata-ges-disc/dataset](./input/earthdata-ges-disc/dataset).

### 5. Build a Model

TBA

## References

1. [How to Query and Use NASA Geo-Data for Your Next Data Science Project](https://medium.com/@sirmammingtonham/how-to-query-and-use-nasa-geo-data-for-your-next-data-science-project-27aef13c93d2) by [Ethan Joseph](https://medium.com/@sirmammingtonham)
1. [Getting NASA data for your next geo-project](https://towardsdatascience.com/getting-nasa-data-for-your-next-geo-project-9d621243b8f3) by [Karan Bhanot](https://medium.com/@bhanotkaran22)
1. [Wikipedia: Hydroelectric stations owned by BC Hydro](https://en.wikipedia.org/wiki/List_of_generating_stations_in_British_Columbia)
1. [Goddard Earth Sciences Data and Information Services Center (GES DISC) data collections search](https://disc.gsfc.nasa.gov/)
1. [GES DISC - GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V06 (GPM_3IMERGDL) - Summary](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_06/summary)
1. [GES DISC - GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V06 (GPM_3IMERGDL) - README](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/doc/README.GPM.pdf)
1. [GES DISC - How to Access GES DISC Data Using wget and curl](https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Access%20GES%20DISC%20Data%20Using%20wget%20and%20curl)
1. [GES DISC - How to Generate Earthdata Prerequisite Files](https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Generate%20Earthdata%20Prerequisite%20Files)
