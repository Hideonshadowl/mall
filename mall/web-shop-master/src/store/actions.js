import * as type from './types'
const action = {
  addcart({commit}, val) {
    commit(type.ADDCART, val);
  },
  savepw({commit}, val) {
    commit(type.SAVEPW, val);
  },
  showthis({commit}, val) {
    commit(type.SHOWTHIS, val);
  },
}
export default action
