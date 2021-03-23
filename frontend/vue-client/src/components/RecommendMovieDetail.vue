<template>
  <div class="recommend-movie">
    <marquee behavior="scroll" direction="" class="size">
      <h1 style="color:#F2AC29">👍</h1></marquee>
    <div class="detail-image" @click="getMovieId">
      <div>
        <img :src="posterURI" alt="">
      </div>
      <div class="recommend-movie-detail">
        {{ movie.title }}
        <br>
        <p>{{ movie.vote_average }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecommendMovieDetail',
  props: {
    movie: Object,
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
    
      axios.get(`http://127.0.0.1:8000/movies/${movieId}`, config)
        .then(res => {
          this.selectedMovie = res.data
          console.log(res.data)
          if (this.$router.push({ name: 'DetailMovie'}) !=='/detail' )
            this.$router.replace({ name: 'DetailMovie', query: this.selectedMovie})
        })
    }
  },
  computed: {
    posterURI() {
      const posterId = this.movie.poster_path
      return `https://image.tmdb.org/t/p/w200/${posterId}`
    },
  },
}
</script>

<style scoped>

  .size {
    width: 30px;
  }
  .recommend-movie-detail {
    margin: 10px;
    font-weight: bold;
    font-size: 20px;
  }

  p {
  margin-top: 1px;
  color: rgb(212, 44, 86);
  }

  .detail-image {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;  
}

.detail-image:hover {
  transform: scale(1.2);
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -o-transform: scale(1.2);
}
img {
  height: 480px;
  width: 320px;
  border-radius: 25px;
  margin-top: 10px;
  margin-left: 10px;
  margin-right: 10px;
  overflow:hidden;
}

</style>