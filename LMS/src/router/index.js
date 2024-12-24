import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/courses',
    name: 'Courses',
    component: () => import('../views/Courses.vue')
  },
  {
    path: '/students',
    name: 'Students',
    component: () => import('../views/Students.vue')
  },
  {
    path: '/assignments',
    name: 'Assignments',
    component: () => import('../views/Assignments.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 