import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import gzip

# Only if needed
# movies = pd.read_csv(r"D:\MY WORK\DATA SCIENCE PROJECT\MOVIE RECOMMENDATION\Movie Recommender.csv")
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)
new_df = pd.read_csv('D:\MY WORK\DATA SCIENCE PROJECT\MOVIE RECOMMENDATION\Movie Recommender')

def get_recommendation(movie):
    try:
        movie_index = new_df[new_df['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = [new_df.loc[i[0], 'title'] for i in movie_list]
        return recommended_movies
    except IndexError:
        return ["Movie not found"]

st.title("🎬 Movie Recommender System")
st.header("Find Your Next Favorite Movie")

selected_movie = st.selectbox("Select a movie:", new_df['title'].values)

if st.button("Recommend"):
    recommendations = get_recommendation(selected_movie)
    st.write(f"Because you liked **{selected_movie}**, you might also like:")
    for rec in recommendations:
        st.write(f"- {rec}")