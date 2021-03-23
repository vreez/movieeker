<template>
   <div>
      <div @click="getMovieId">
        <div class="image">
          <div>
            <img :src="posterURI" alt=""> 
          </div>  
          <br>
          <div class="movie-title-vote">
            <p class="movie-title">{{ movie.title }}</p>
            <p>{{ movie.vote_average }}</p>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'NowPlaying',
  props: {
    movie: Object,
  },
  data () {
    return {
      selectedMovie: '',
    }
  },
  computed: {
    posterURI() {
      const posterId = this.movie.poster_path
      return `https://image.tmdb.org/t/p/w200/${posterId}`
    }
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getMovieId() {
      const config = this.setToken()
      const movieId = this.movie.movie_id
      console.log(movieId)
      axios.get(`http://127.0.0.1:8000/movies/${movieId}`, config)
        .then(res => {
          console.log('detail을위한movieid불러오기')
          this.selectedMovie = res.data
          if (this.$router.push({ name: 'DetailMovie'}) !=='/detail' )
            this.$router.replace({ name: 'DetailMovie', query: this.selectedMovie})
        })
    }
  }
}
</script>

<style>
.movie {
  border: teal 1px solid;
  float: left;
}

.image {
  float: left;
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;  
}

.image:hover {
  transform: scale(1.2);
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -o-transform: scale(1.2);
  cursor: pointer;
}
img {
  height: 400px;
  width: 280px;
  border-radius: 25px;
  margin-top: 10px;
  margin-left: 10px;
  margin-right: 10px;
  overflow:hidden;

}

.movie-title-vote {
  font-weight: bold;
  font-size: 18px;
}

p {
  margin-top: 1px;
  color: rgb(212, 44, 86);
}

.movie-title{
  margin-bottom: 0;
  color: black;
  font-weight: bold;
  width: 280px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>