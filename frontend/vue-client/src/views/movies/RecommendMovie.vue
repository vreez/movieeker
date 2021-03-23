<template>
  <div>
    <div class="main">
      <h1 class="main-title" style="font-weight:bold">당신의 취향을 반영한 영화</h1>
    </div>
    <div>
      <b-button id="tooltip-target" class="random-btn" variant="warning" @click="getRandom">❓❓❓</b-button>
      <b-tooltip target="tooltip-target" triggers="hover">
        내가 <b>궁금한가요?</b><br>클릭해보세요!
      </b-tooltip>
      <RecommendRandom v-if="isMovie"
        :movie="randomMovie"
        :isMovie="isMovie"
      />
    </div>
    <br>
    <h2 class="recommend-title">인기 있는건 다 넣었어</h2>
    <div class="recommend">
      <RecommendMovieDetail 
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
      />
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import RecommendMovieDetail from '@/components/RecommendMovieDetail'
import RecommendRandom from '@/components/RecommendRandom'

export default {
  name: 'recommend',
  components: {
    RecommendMovieDetail,
    RecommendRandom,
  },
  data() {
    return {
      movies: '',
      randomList: [],
      randomMovie: [],
      isMovie: false,
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
    getRecommend() {
      const config = this.setToken()
      axios.get(`http://127.0.0.1:8000/movies/recommend`, config)
        .then(res => {
          this.movies = res.data
        })
    },
    getRandom() {
      const config = this.setToken()
      axios.get('http://127.0.0.1:8000/movies/random/', config)
        .then(res => {
          console.log('추천')
          console.log(res.data)
          this.randomList = res.data
          const randomIndex = _.random(this.randomList.length - 1)
          this.randomMovie = this.randomList[randomIndex]
          this.isMovie = true
          console.log(this.randomMovie)
        })
    },
    
    
  },
  created() {
    this.getRecommend()    
  },
  
}
</script>

<style scoped>

  .recommend-title {
    font-weight: bold;
    margin-bottom: 30px;
  }
  .recommend {
    margin-bottom: 200px;
    display: inline-block;
  }

  .random-btn {
    padding: 10px 15px;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .main {
    height: 400px;
    background-image: url(https://i.pinimg.com/originals/68/84/52/688452f0ace187c8b68a89e987ec3e7e.gif);
    margin-bottom: 20px;
    background-size: 1920px;
    filter: grayscale(100%);
  }

  .main-title {
    color:white;
    position: relative;
    padding-top: 180px;
    font-weight: bold;
  }

</style>