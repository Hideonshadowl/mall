<template>

  <div>

        <div class="search-header" style="position: fixed">
          <i class="iconfont icon-left" @click="goBack"></i>
          <div class="search-con">
            <i class="iconfont icon-search"></i>
            <input v-focus placeholder="" v-model="searchText" />
          </div>
          <span @click="">搜索</span>
        </div>


        <div style="display: flex;flex-wrap: wrap;margin-top: 1.5rem" >
          <div @click="showgood" class="content" style=":order: a;width: 50%;box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);height: 5rem" v-for="a in productList">
            <img style="width: 3.5rem;height: 3.5rem;margin-left: 0.8rem" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574161425237&di=e28618fc970343d607baaeaf40697078&imgtype=0&src=http%3A%2F%2Fimg1.juimg.com%2F160118%2F330718-16011QRF647.jpg" alt="">
            <p style="font-size: 0.4rem;margin-left: 0.8rem">{{a}}</p>
            <p style="font-size: 0.4rem;margin-left: 0.8rem">$88.00</p>
          </div>
        </div>

  </div>

</template>

<script>


  import {mapMutations} from 'vuex'
  export default {
    data() {
      return {
        searchText:'',
        keyword: '',
        productList: ['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b'],
        orderBy: 'default',
        params: {
          categoryId: '',
          keyword: '',
          pageNum: 1,
          pageSize: 20,
          orderBy: 'default'
        },
        isLoading: true,
        seclectActive: false,
        searchBtn: false,
        messageText: '',
        isMessage: false
      }
    },
    created() {
        if (this.$route.query.search_value) { this.productList=[this.$route.query.search_value] }
    },
    mounted() {

      },
    methods: {
      ...mapMutations([
        'RECORE_FOOT'
      ]),
      showgood(){
        this.$router.push('./product-detail')
      },
      goBack(){this.$router.push('./home')}
      },
      //价格排序
      selectOrder(e) {
        let orderBy = e.currentTarget.getAttribute('data-orderBy')
        if (orderBy === this.orderBy) {
          return
        }
        this.productList = []    //重置list
        this.orderBy = orderBy
        this.params.orderBy = orderBy
        this.params.pageNum = 1
        this.isLoading = true
        this.getProductList(this.params)
      },

      showMessage() {
        this.isMessage = true
        this.messageText = '没有更多的商品啦！'
        setTimeout(() => {
          this.isMessage = false
        }, 1200)
      },
      getSearch() {
        this.$router.push('/product-list?keyword=' + this.keyword + '&categoryId=0')
        // // console.log(1111)
        this.params.keyword = this.keyword
        this.params.pageNum = 1
        this.productList = []
        this.getProductList(this.params)
      },

      //刷新
      onRefresh(done) {
        this.params.pageNum = 1
        this.productList = []
        this.isLoading = true
        this.getProductList(this.params);
        done() // call done
      },
      //加载更多
      onInfinite(done) {
        this.params.pageNum++
        this.getProductList(this.params);
        done()
      },
      pageScroll() {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
        scrollTop > 100 ? this.seclectActive = true : this.seclectActive = false
      },
      textEnter() {
        this.searchBtn = true
      },
      textLeave() {
        this.searchBtn = false
      },
      goBack() {
        console.log(111)
        this.$router.go(-1)
      }

  }
</script>

<style lang="scss" type="text/scss" scoped>
  @import '../../common/style/mixin';

  .search-header {
    @include fj;
    width: 100%;
    height: 90px;
    padding: 15px 30px 15px 20px;
    box-sizing: border-box;
    @include border-1px(#dcdcdc);
    .icon-left {
      width: 10%;
      font-size: 50px;
      color: #252525;
      font-weight: bold;
    }
    .search-con {
      width: 76%;
      height: 100%;
      line-height: 60px;
      margin-left: -20px;
      padding-left: 30px;
      font-size: 26px;
      background: #F7F7F7;
      border-radius: 40px;
      @include boxSizing;
      .iconfont {
        font-size: 36px;
        padding-right: 20px;
      }
      input {
        font-size: 24px;
        background: #F7F7F7;
      }
    }
    span{
      width: 12%;
      text-align: center;
      height: 100%;
      line-height: 60px;
      color: #fff;
      font-size: 26px;
      background: #E93B3D;
      border-radius: 10px;
    }
  }
</style>
