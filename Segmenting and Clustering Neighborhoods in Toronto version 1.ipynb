{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#importing Libraries\n",
    "import requests\n",
    "import lxml.html as lh\n",
    "import bs4 as bs\n",
    "import urllib.request\n",
    "import numpy as np \n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Getting the data from url\n",
    "url = \"https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M\"\n",
    "res = requests.get(url)\n",
    "soup = bs.BeautifulSoup(res.content,'lxml')\n",
    "table = soup.find_all('table')[0]\n",
    "df = pd.read_html(str(table))\n",
    "data = pd.read_json(df[0].to_json(orient='records'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighbourhood</th>\n",
       "      <th>Postcode</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Not assigned</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>M1A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Not assigned</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>M2A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>North York</td>\n",
       "      <td>Parkwoods</td>\n",
       "      <td>M3A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>North York</td>\n",
       "      <td>Victoria Village</td>\n",
       "      <td>M4A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Downtown Toronto</td>\n",
       "      <td>Harbourfront</td>\n",
       "      <td>M5A</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Borough     Neighbourhood Postcode\n",
       "0      Not assigned      Not assigned      M1A\n",
       "1      Not assigned      Not assigned      M2A\n",
       "2        North York         Parkwoods      M3A\n",
       "3        North York  Victoria Village      M4A\n",
       "4  Downtown Toronto      Harbourfront      M5A"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#First 5 records\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Choosing only data where field Borough doesn't have not assigned value\n",
    "raw_data_selected = data[data['Borough'] != 'Not assigned']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Grouping Data\n",
    "raw_data_selected = raw_data_selected.groupby(['Borough', 'Postcode'], as_index=False).agg(','.join)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Borough</th>\n",
       "      <th>Postcode</th>\n",
       "      <th>Neighbourhood</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Central Toronto</td>\n",
       "      <td>M4N</td>\n",
       "      <td>Lawrence Park</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Central Toronto</td>\n",
       "      <td>M4P</td>\n",
       "      <td>Davisville North</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Central Toronto</td>\n",
       "      <td>M4R</td>\n",
       "      <td>North Toronto West</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Central Toronto</td>\n",
       "      <td>M4S</td>\n",
       "      <td>Davisville</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Central Toronto</td>\n",
       "      <td>M4T</td>\n",
       "      <td>Moore Park,Summerhill East</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Borough Postcode               Neighbourhood\n",
       "0  Central Toronto      M4N               Lawrence Park\n",
       "1  Central Toronto      M4P            Davisville North\n",
       "2  Central Toronto      M4R          North Toronto West\n",
       "3  Central Toronto      M4S                  Davisville\n",
       "4  Central Toronto      M4T  Moore Park,Summerhill East"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw_data_selected.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Replacing values in Neighbourhood field with Borough where Neighbourhood is not assigned\n",
    "raw_data_selected['Neighbourhood'] = np.where(raw_data_selected['Neighbourhood'] == 'Not assigned', raw_data_selected['Borough'], raw_data_selected['Neighbourhood'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(103, 3)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Shape of Data\n",
    "raw_data_selected.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
