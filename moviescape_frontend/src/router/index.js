import Vue from 'vue'
import VueRouter from 'vue-router'

// Home
import HomeView from '@/views/HomeView.vue'

// Movie
import MovieDetailView from '@/views/Movie/MovieDetailView.vue'
import MovieListView from '@/views/Movie/MovieListView.vue'
import GenreListView from '@/views/Movie/GenreListView.vue'

// Human
import ActorListView from '@/views/Human/ActorListView.vue'
import DirectorListView from '@/views/Human/DirectorListView.vue'
import ActorDetailView from '@/views/Human/ActorDetailView.vue'
import DirectorDetailView from '@/views/Human/DirectorDetailView.vue'

// Review
import ReviewListView from '@/views/Review/ReviewListView.vue'
import CreateReviewView from '@/views/Review/CreateReviewView.vue'

// Recommend
import RecommendView from '@/views/Recommend/RecommendView.vue'

// Account
import LoginView from '@/views/Account/LoginView.vue'
import SignUpView from '@/views/Account/SignUpView.vue'
import UserDetailView from '@/views/Account/UserDetailView.vue'
import MyDetailView from '@/views/Account/MyDetailView.vue'

// Recommend, Random
import RandomProfileVue from '@/components/RandomProfile.vue';

//###
import TesT from '@/components/TesT.vue'




Vue.use(VueRouter)

const routes = [
  // Home
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  // ###############

  // Movie
  {
    path: '/MovieListView',
    name: 'MovieListView',
    component: MovieListView
  },
  {
    path: '/MovieDetailView',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/GenreListView',
    name: 'GenreListView',
    component: GenreListView
  },
  // ###############

  // Human
  {
    path: '/ActorListView',
    name: 'ActorListView',
    component: ActorListView
  },
  {
    path: '/DirectorListView',
    name: 'DirectorListView',
    component: DirectorListView
  },
  {
    path: '/ActorDetailView',
    name: 'ActorDetailView',
    component: ActorDetailView
  },
  {
    path: '/DirectorDetailView',
    name: 'DirectorDetailView',
    component: DirectorDetailView
  },



  // ###############

  // Review
  {
    path: '/ReviewListView',
    name: 'ReviewListView',
    component: ReviewListView
  },
  {
    path: '/CreateReviewView',
    name: 'CreateReviewView',
    component: CreateReviewView
  },
  // ###############

  // Recommend
  {
    path: '/RecommendView',
    name: 'RecommendView',
    component: RecommendView
  },
  // ###############

  // Account
  {
    path: '/LoginView',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/SignUpView',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/UserDetailView',
    name: 'UserDetailView',
    component: UserDetailView
  },
  {
    path: '/MyDetailView',
    name: 'MyDetailView',
    component: MyDetailView
  },
  
  // #######
  // Recommend, Random
  {
    path: '/RandomProfileVue',
    name: 'RandomProfileVue',
    component: RandomProfileVue
  },

  // ###############  
  // test용 라우터
  {
    path: '/TesT',
    name: 'TesT',
    component: TesT
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
