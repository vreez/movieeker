import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import PostList from '@/views/community/PostList'
import CreatePost from '@/views/community/CreatePost'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import DetailMovie from '@/views/movies/DetailMovie'

import Detail from '@/views/community/Detail'
import MovieList from '@/views/movies/MovieList'
import RecommendMovie from '@/views/movies/RecommendMovie'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/PostList',
    name: 'PostList',
    component: PostList,
  },
  {
    path: '/community/create/:id?',
    name: 'CreatePost',
    component: CreatePost,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/detailmovie',
    name: 'DetailMovie',
    component: DetailMovie,
    props: true
  },
  {
    path: '/community/:id',
    name: 'Detail',
    component: Detail
  },
  {
    path: '/movielist',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/recommendmovie',
    name: 'RecommendMovie',
    component: RecommendMovie,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
