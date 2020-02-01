<template>

  <div>

        <div class="search-header" >
          <i class="iconfont icon-left" @click="goBack"></i>
<!--          <div class="search-con">-->
<!--            <i class="iconfont icon-search"></i>-->
<!--            <input v-focus placeholder="" v-model="searchText" />-->
<!--          </div>-->
<!--          <span @click="">搜索</span>-->
        </div>


      <section class="floor-list" style="">
        <div class="floor-content">
          <div class="floor-category" v-for="singlewine in this.productList" @click="showgood(singlewine)">
            <div class="floor-products">
              <img style="width: 3rem;height: 3rem" :src=singlewine.img_url  alt="">
            </div>
            <p>{{singlewine.price}}¥</p>
            <p>{{singlewine.name}}</p>
          </div>
        </div>
      </section>

  </div>

</template>

<script>


  import {mapActions} from 'vuex'
  import { mapState } from 'vuex'
  export default {
    computed: mapState(['foodlist']),
    data() {
      return {
        searchText:'',
        keyword: '',
        productList: [],
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
        console.log(this.thiscategory);
        if (this.$route.query.search_value) { this.productList=[this.$route.query.search_value] }
    },
    destroyed() {

    },
    mounted() {
          this.foodlist.forEach(val=>{
            if(val.category===this.$route.query.category){
              this.productList.push(val)
            }
          })
      },
    methods: {
      ...mapActions(['clearlist']),
      showgood(item){
        this.$router.push({
            path:'./product-detail',
            query:{
              good:item
            }
          }
        )
      },
      goBack(){
        this.$router.push('./home')}
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
  .floor-list {
    width: 100%;
    padding-bottom: 100px;
    .floor-head {
      width: 100%;
      height: 80px;
      background: #F6F6F6;
    }
    .floor-content {
      display: flex;
      flex-shrink: 0;
      flex-wrap: wrap;
      width: 100%;
      @include boxSizing;
      .floor-category {
        width: 50%;
        padding: 20px;
        border-right: 1px solid #dcdcdc;
        border-bottom: 1px solid #dcdcdc;
        @include boxSizing;
        &:nth-child(2n) {
          border-right: none;
        }
        p {
          font-size: 34px;
          color: #333;
          &:nth-child(2) {
            padding: 10px 0;
            font-size: 26px;
            color: $red;
          }
        }
        .floor-products {
          display: flex;
          justify-content: space-around;
          width: 100%;
          img {
            width: 130px;
            height: 130px;
          }
        }
      }
    }
  }
</style>
