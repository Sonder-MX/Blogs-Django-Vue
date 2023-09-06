import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"
import pinia from "./stores"

URLSearchParams.prototype.appendIfExists = function (key, value) {
  if (value !== null && value !== undefined) {
    this.append(key, value)
  }
}

createApp(App).use(router).use(pinia).mount("#app")
