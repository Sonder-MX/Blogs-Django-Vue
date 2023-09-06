import { defineStore } from "pinia"

const useUserStore = defineStore("userStore", {
  state: () => ({
    token: localStorage.getItem("blog.token") || null,
    refreshToken: localStorage.getItem("blog.refresh") || null,
    username: localStorage.getItem("blog.username") || null,
    tokenExp: localStorage.getItem("blog.tokenExp") || "", // token过期时间
  }),
  getters: {},
  actions: {},
})

export default useUserStore
