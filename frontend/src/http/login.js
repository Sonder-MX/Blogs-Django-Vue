import request from "."

// 用户登录
export const reqLogin = (data) => request.post("/token/", data)

// 用户注册
export const reqRegister = (data) => request.post("/user/", data)
