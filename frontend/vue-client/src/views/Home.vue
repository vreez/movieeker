<template>
  <div class="background">
    <div>
        <div class="main-title" style="color: rgb(66, 66, 233)"><b>what's <br>your<br>favorite?<br></b>
        <marquee behavior="scroll" direction="" class="size">
        <h1 style="color:#FF584C">✨WELCOME! If you want to see movie, you're already MOVIEEKER!✨</h1></marquee>
        </div>
      </div>
    <div class="main-bg">
      <div class="blob">
        <svg xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 350">
        <path d="M156.4,339.5c31.8-2.5,59.4-26.8,80.2-48.5c28.3-29.5,40.5-47,56.1-85.1c14-34.3,20.7-75.6,2.3-111  c-18.1-34.8-55.7-58-90.4-72.3c-11.7-4.8-24.1-8.8-36.8-11.5l-0.9-0.9l-0.6,0.6c-27.7-5.8-56.6-6-82.4,3c-38.8,13.6-64,48.8-66.8,90.3c-3,43.9,17.8,88.3,33.7,128.8c5.3,13.5,10.4,27.1,14.9,40.9C77.5,309.9,111,343,156.4,339.5z"/>
        </svg>
      </div>
    </div>
    <div class="home-movie">
      <HomeMovie />
    </div>
    <br>
    <div class="quote-box">
      <p class="quote">사진은 진실이다. <br>영화는 1초에 24개의 진실을 담는다. <br></p>
      <h5>- 장 뤽 고다르 -</h5>
    </div>
    <div class="gifs">
      <img class="gif" src="https://i.pinimg.com/originals/5a/6c/2d/5a6c2d683ebeb49e9bd3e6390f180402.gif" alt="">
      <img class="gif" src="https://i.pinimg.com/originals/5a/6c/2d/5a6c2d683ebeb49e9bd3e6390f180402.gif" alt="">
    </div>
  </div>
</template>

<script>
import HomeMovie from '@/components/HomeMovie'

export default {
  name: 'Home',
  data() {
    return {
      rating: 0
    }
  },
  components: {
    HomeMovie,
  },
  props: {
  },
}
</script>

<style scoped>
  .main-bg {
    width: 1920px;
  }

  .background {
    padding-top: -100px;
  }
  .home-movie {
    vertical-align: middle;
    text-align: center;
    margin-bottom: 200px;
  }
  template { 
    margin:0; 
    padding:0; 
    width:100%; 
    height:100% 
  }

  @import url('https://fonts.googleapis.com/css?family=Poppins:700');

  .main-title {
    color: rgb(66, 66, 233);
    font-size: 20vmin;
    line-height: 1;
    font-weight: bold;
    letter-spacing: 2px;
    font-family: 'Poppins', sans-serif;
    text-transform: uppercase;
    padding-left: 40px;
    margin-left: 20px;
    height: 1000px;
    margin-top:100px;
  }

  .blob {
    position: absolute;
    top: 0;
    left: 0;
    fill: #113957;
    width: 50vmax;
    z-index: 1;
    animation: move 10s ease-in-out infinite;
    transform-origin: 50% 50%;
    overflow: visible;
    line-height: 1.1;
  }

  @keyframes move {
    0%   { transform: scale(1)   translate(10px, -30px); }
    38%  { transform: scale(0.8, 1) translate(80vw, 30vh) rotate(160deg); }
    40%  { transform: scale(0.8, 1) translate(80vw, 30vh) rotate(160deg); }
    78%  { transform: scale(1.3) translate(0vw, 50vh) rotate(-20deg); }
    80%  { transform: scale(1.3) translate(0vw, 50vh) rotate(-20deg); }
    100% { transform: scale(1)   translate(10px, -30px); }
  }
  .text {
    z-index: 1;
    margin-top: 150px;
  }
  .size {
    width: 600px;
  }

  @import url('https://fonts.googleapis.com/css?family=Poppins:700');
  body {
    margin: 0;
    padding: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    position: relative;
    background: #FFB1A4;
    
    display: flex;
    align-items: center;
  }

  .main-title {
    color: rgb(66, 66, 233);
  }

  .blob {
    position: absolute;
    top: 0;
    left: 0;
    fill: #FFB1A4;
    width: 50vmax;
    z-index: -1;
    animation: move 10s ease-in-out infinite;
    transform-origin: 50% 50%;
  }

  @keyframes move {
    0%   { transform: scale(1)   translate(10px, -30px); }
    38%  { transform: scale(0.8, 1) translate(80vw, 30vh) rotate(160deg); }
    40%  { transform: scale(0.8, 1) translate(80vw, 30vh) rotate(160deg); }
    78%  { transform: scale(1.3) translate(0vw, 50vh) rotate(-20deg); }
    80%  { transform: scale(1.3) translate(0vw, 50vh) rotate(-20deg); }
    100% { transform: scale(1)   translate(10px, -30px); }
  }
  .quote {
    font-size: 40px;
    color: black;
    font-weight: 800;
  }

  .quote-box {
    margin-bottom: 350px;
  }

  .footer {
    height: 250px;
    background: rgb(20, 20, 20);
  }

  .words-in-footer {
    vertical-align: middle;
    padding-top: 120px;
  }

  .gifs {
    margin-bottom: 400px;
  }

  .gif {
    width: 500px;
    height: 278px;
    border-radius: 0%;
  }
  
</style>