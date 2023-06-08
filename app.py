import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Fungsi untuk melakukan analisis data
def analyze_data(data):
    # ANOVA
    st.header('Analisis ANOVA')
    group_means = data.groupby('X')['Y'].mean()
    st.write('Mean per group:')
    st.write(group_means)
    st.write('One-way ANOVA:')
    result_anova = stats.f_oneway(*[data[data['X'] == x]['Y'] for x in data['X'].unique()])
    st.write('F-value:', result_anova.statistic)
    st.write('p-value:', result_anova.pvalue)

    # Korelasi
    st.header('Analisis Korelasi')
    correlation = data.corr()
    st.write('Matriks Korelasi:')
    st.write(correlation)
    sns.heatmap(correlation, annot=True, cmap='coolwarm', square=True)
    st.pyplot()

    # Regresi
    st.header('Analisis Regresi')
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['X'], data['Y'])
    st.write('Slope:', slope)
    st.write('Intercept:', intercept)
    st.write('R-value:', r_value)
    st.write('p-value:', p_value)
    st.write('Standard Error:', std_err)

    # Visualisasi Data
    st.header('Visualisasi Data')
    st.subheader('Histogram')
    plt.hist(data['X'], bins='auto', alpha=0.7, rwidth=0.85)
    plt.xlabel('X')
    plt.ylabel('Frequency')
    st.pyplot()

    st.subheader('Scatter Plot')
    plt.scatter(data['X'], data['Y'])
    plt.xlabel('X')
    plt.ylabel('Y')
    st.pyplot()

# Main program
def main():
    st.title('ANOVA REGRESI KORELASI')
    st.write('Im not lazy, Im just on energy-saving mode! yukk excellent nyaa ditunggu xixixiixi')

    # Input data manual
    st.header('Input Data Manual \nJumlah data X = Jumlah data Y')
    num_points = st.number_input('Jumlah titik data', min_value=1, step=1, value=100)
    data = pd.DataFrame()
    data['X'] = st.multiselect('Pilih nilai X', list(range(1, 100)), [], key='X')
    data['Y'] = st.multiselect('Pilih nilai Y', list(range(1, 100)), [], key='Y')
    data = data.sample(num_points, replace=True)

    # Menampilkan data
    st.header('Data')
    st.write(data)

    if len(data) > 1:
        # Analisis data
        analyze_data(data)
    else:
        st.write('Masukkan setidaknya 2 titik data untuk melakukan analisis.')

if __name__ == '__main__':
    main()