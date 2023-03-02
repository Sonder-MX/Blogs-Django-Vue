import { sendPostReq, sendGetReq } from "@/http"

async function authorization() {
  const storage = localStorage

  let hasLogin = false
  let userName = storage.getItem("username.myblog")

  const expiredTime = Number(storage.getItem("expiredTime.myblog"))
  const refreshToken = storage.getItem("refresh.myblog")

  // token 未过期
  if (expiredTime > Date.now()) {
    hasLogin = true
  }
  // token 过期  申请刷新 token
  else if (refreshToken !== null) {
    try {
      let response = sendPostReq("/token/refresh/", { refresh: refreshToken })

      const nextExpiredTime = Date.now() + 60000 * 60
      storage.setItem("access.myblog", response.data.access)
      storage.setItem("expiredTime.myblog", nextExpiredTime)
      sendGetReq("/user/" + userName + "/").then((resp) => {
        storage.setItem("isSuperuser.myblog", resp.data.is_superuser)
      })
      storage.removeItem("refresh.myblog")

      hasLogin = true
    } catch (err) {
      storage.clear()
      hasLogin = false
      console.log("authorization err")
    }
  }
  // 无任何有效 token
  else {
    storage.clear()
    hasLogin = false
    console.log("authorization exp")
  }

  return [hasLogin, userName]
}

export default authorization
