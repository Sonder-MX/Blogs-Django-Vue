import axios from "axios"

const tagUrl = "http://127.0.0.1:8000/api"

export const sendGetReq = async (resUrl) => {
  const response = await axios.get(tagUrl + resUrl)
  return response.data
}

export const sendPostReq = async (surl, payload, config_obj = "") => {
  return await axios.post(tagUrl + surl, payload, config_obj)
}

export const sendPutReq = async (surl, payload, config_obj) => {
  return await axios.put(tagUrl + surl, payload, config_obj)
}

export const sendPatchReq = async (surl, payload, config_obj) => {
  return await axios.patch(tagUrl + surl, payload, config_obj)
}

export const sendDeleteReq = async (surl, config_obj) => {
  return await axios.delete(tagUrl + surl, config_obj)
}

const baseUrl = "http://127.0.0.1:8000/api"

// 对axios二次封装
const request = axios.create({
  baseURL: baseUrl,
  timeout: 10000,
})

// 请求拦截器
request.interceptors.request.use((config) => {
  return config
})

// 响应拦截器
request.interceptors.response.use(
  (response) => {
    return Promise.resolve(response.data)
  },
  (error) => {
    const status = error.response.status // 错误状态码
    // todo 错误处理
    return Promise.reject(error)
  }
)

export default request
