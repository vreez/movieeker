<template>
  <div id="app">
    <div>
      <b-navbar toggleable="lg" type="light" variant="transparent">
      <b-navbar-brand href="#" style="font-weight:bold, color:red"><router-link to="/">
      <div class="loading">
        <h1 class="main-title" style="font-weight:bold">
          <span>M</span>
          <span>O</span>
          <span>V</span>
          <span>I</span>
          <span>E</span>
          <span>E</span>
          <span>K</span>
          <span>E</span>
          <span>R</span>
        </h1>
      </div>
      </router-link></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class=" ml-auto">
            <b-navbar-nav v-if="login">
              <li><a href="#"><router-link to="/movielist" class="nav-detail">Movie List</router-link></a></li>
              <li><a href="#"><router-link to="/recommendmovie" class="nav-detail">Recommend Movie </router-link></a></li>
              <li><a href="#"><router-link :to="{ name: 'PostList' }" class="nav-detail">Post List</router-link></a></li>
              <li><a href="#"><router-link :to="{ name: 'CreatePost' }" class="nav-detail">Create Post</router-link></a></li>
              <li><a href="#"><router-link @click.native="logout" to="#" class="nav-detail">Logout</router-link></a></li>
            </b-navbar-nav>
            <b-navbar-nav v-else>
              <li><a href="#"><router-link to="/signup" class="nav-detail">SignUp</router-link></a></li>
              <li><a href="#"><router-link to="/login" class="nav-detail">Login</router-link></a></li>
            </b-navbar-nav>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <router-view @login="login = true" />
    
    <div class="footer">
      <div class="words-in-footer">
        <h6 style="color:white">영화추천 사이트 MOVIEEKER입니다.</h6>
        <h6 style="color:white">© All right Reversed TEAM MOVIEEKER with SSAFY.</h6>
        <h6 class="chrome" style="color:white">[ 원활한 이용을 위해 Chrome사용을 권장합니다. ]</h6>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      login: false
    }
  },
  components: {

  },
  methods: {
    logout() {
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created() {
    // 로그인 되어있는 상태인지 확인! >>> 서버로부터 JWT 받았는지 확인!
    const token = localStorage.getItem('jwt')
    
    // token 이 있으면?
    if (token) {
      // login 상태 변수를 true
      this.login = true
    }
  }
}
</script>

<style>
  body {
    background-color: rgb(255, 255, 255);
  }
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color:#3F67E0;
  }

  html,body{padding:0; margin:0;}
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  h1{color:#3F67E0;}
  table{width:50%; border-collapse:collapse; margin: 0 auto;}
  .wrap{width:50%;}
  .container{width:800px; margin:0 auto;}
  a{text-decoration:none;}
  .btn{padding:10px; background:#34445c; color:#fff;}


  .footer {
    height: 290px;
    background: rgb(20, 20, 20);
    margin-bottom: 0;
    margin-top:auto;
  }

  .chrome {
    font-size: 13px;
    margin-top: 15px;
  }

  .words-in-footer {
    vertical-align: middle;
    padding-top: 120px;
  }

  .nav-detail {
    font-weight: bold;
    color: #FF584C;
    font-size: 17px;
  }

  .loading {
    margin-left: 50px;
  }

  .loading span {
    display: inline-block;
    margin: 0 -.075em;
    animation: loading .9s infinite alternate;
  }
  .loading span:nth-child(2) {
    animation-delay: .1s;
  }
  .loading span:nth-child(3) {
    animation-delay: .2s;
  }
  .loading span:nth-child(4) {
    animation-delay: .3s;
  }
  .loading span:nth-child(5) {
    animation-delay: .4s;
  }
  .loading span:nth-child(6) {
    animation-delay: .5s;
  }
  .loading span:nth-child(7) {
    animation-delay: .6s;
  }
  .loading span:nth-child(8) {
    animation-delay: .7s;
  }
  .loading span:nth-child(9) {
    animation-delay: .8s;
  }
  @keyframes loading {
    0% {
      transform: scale(1);
    }
    100% {
      transform: scale(0.8);
    }
  }

nav ul {
  list-style: none;
  text-align: center;
}
nav ul li {
  display: inline-block;
}
nav ul li a {
  display: block;
  padding: 15px;
  text-decoration: none;
  color: #aaa;
  font-weight: 800;
  text-transform: uppercase;
  margin: 0 10px;
}
nav ul li a,
nav ul li a:after,
nav ul li a:before {
  transition: all .5s;
}
nav ul li a:hover {
  color: #555;
}

nav.stroke ul li a,
nav.fill ul li a {
  position: relative;
}
nav.stroke ul li a:after,
nav.fill ul li a:after {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  width: 0%;
  content: '.';
  color: transparent;
  background: #aaa;
  height: 1px;
}
nav.stroke ul li a:hover:after {
  width: 100%;
}

</style>
