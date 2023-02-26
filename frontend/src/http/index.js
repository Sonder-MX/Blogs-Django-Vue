import axios from "axios"
import { reactive } from "vue"

const tagUrl = "http://127.0.0.1:8000/api"

export const reqArticleListOrDetail = async (resUrl) => {
  const response = await axios.get(tagUrl + resUrl)
  return response.data
}

export const sendPostReq = async (surl, payload) => {
  return await axios.post(tagUrl + surl, payload)
}
