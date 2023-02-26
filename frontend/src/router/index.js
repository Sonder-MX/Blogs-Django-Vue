import { createWebHistory, createRouter } from "vue-router"

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/Home.vue"),
  },
  {
    path: "/article/:id",
    name: "ArticleDetail",
    component: () => import("@/views/ArticleDetail.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/Login.vue")
}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
