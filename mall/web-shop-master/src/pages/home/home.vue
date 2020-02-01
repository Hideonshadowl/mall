<template>
    <div>
        <header class="home-header wrap" :class="{'active' : headerActive}">
            <router-link tag="i" to="./category" class="iconfont icon-caidan"></router-link>


            <router-link class="header-search" to="./search">
                <i class="iconfont icon-search"></i>
                <router-link tag="span" class="search-title" to="./search">search</router-link>
            </router-link>
            <router-link tag="span" to="./login" v-if="!isLogin">login</router-link>
            <router-link tag="span" to="./user" v-else>
                <i class="iconfont icon-iconyonghu"></i>
            </router-link>
        </header>
        <nav-bar></nav-bar>
        <slider :imgUrl="headList"></slider>

        <swiper :options="swiperOption" style="margin-top: 1rem">
          　　<swiper-slide v-for="(item,index) in swiper_img" :key="index">
          　　　　<img :src=item alt="" style="height: 6.7rem;width: 10rem">
          　　</swiper-slide>
          　　<div class="swiper-pagination" slot="pagination"></div>
        </swiper>


<!--        <el-carousel indicator-position="outside">-->
<!--          <el-carousel-item v-for="item in ['公告1','公告2']" :key="item">-->
<!--            <h3>{{ item }}</h3>-->
<!--          </el-carousel-item>-->
<!--        </el-carousel>-->


        <div style="display: flex;flex-wrap: wrap;margin-left: 0.9rem" >
          <div style="width: 33%;height: 2.7rem" v-for="item in this.categoryList" @click="show(item)">
            <img style="width: 2rem;height: 2rem" :src=item.url alt="">
          </div>
        </div>

        <p style="font-size: 0.5rem;margin-left: 4rem;margin-top: 0.2rem;float: left">店长推荐</p>
        <section class="floor-list" style="position: relative;top: 0.5rem">
                <div class="floor-content">
                    <div class="floor-category" v-for="singlewine in floorList" @click="showgood(singlewine)">
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
    import mHeader from 'components/mHeader'
    import navBar from 'components/navBar'
    import slider from 'components/common/slider'
    import 'swiper/dist/css/swiper.min.css';
    import {mapActions} from 'vuex';
    import { mapState } from 'vuex'
    export default {

        computed: mapState(['foodlist']),

        data() {
            return {
                swiperOption: {
                  pagination: '.swiper-pagination',
                  paginationClickable: true,
                  autoplay: 2500,
                  autoplayDisableOnInteraction: false,
                  loop: false,
                  coverflow: {
                  rotate: 30,
                  stretch: 10,
                  depth: 60,
                  modifier: 2,
                  slideShadows : true
                  }
                },
                swiper_img:["static/lunbo/WechatIMG27.jpeg","static/lunbo/WechatIMG32.jpeg"],
                headList: [],
                categoryList: [{category:"朗姆酒",url:"static/category/lmj.png"},{category:"伏特加",url:"static/category/fjt.png"},{category:"利口酒",url:"static/category/lkj.png"},{category:"特基拉",url:"static/category/tjl.png"},{category:"威士忌",url:"static/category/wsj.png"},{category:"香槟",url:"static/category/xb.png"}],
                floorList: ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a'],
                headerActive: true,
                isLogin: false,
                urll:'static/allimg/48¥ Lubuski Gin 700ml 40vol.png'

            }
        },
        beforeCreate(){

        },
        created(){
        //发起ajax post请求，访问/order/pay，传递参数：order_id
        this.axios.get('http://127.0.0.1:8000/showallwine/')
          .then(data=>{
            this.adddata(data.data.res);
            this.floorList=data.data.res;
          })
          .catch(function (error) {
            console.log(error)
          })
      },
        mounted() {

        },
        methods: {
            ...mapActions(['adddata']),
              show(item){
              this.$router.push({
                path:'./product-list',
                query:{
                  category:item.category
                }
              })
              },
              showgood(item){
              this.$router.push({
                path:'./product-detail',
                query:{
                  good:item
                }
              }
              )
              }
        },
        components: {
            mHeader,
            navBar,
            slider
        }
    }
</script>

<style lang="scss" scoped="" type="text/scss">
    @import '../../common/style/mixin';

    .el-carousel__item h3 {
      margin-left: 2.3rem;
      color: #475669;
      font-size: 2rem;
      opacity: 0.75;
      line-height: 300px;

    }



    .el-carousel__item:nth-child(n) {

    }
    .home-header {
        position: fixed;
        left: 0;
        top: 0;
        @include fj;
        width: 100%;
        height: 100px;
        line-height: 100px;
        padding: 0 30px;
        @include boxSizing;
        font-size: 30px;
        color: #fff;
        z-index: 10000;
        &.active {
           background-color: goldenrod;
        }
        .icon-caidan {
            font-size: 50px;
        }
        .header-search {
            display: flex;
            width: 74%;
            height: 40px;
            line-height: 40px;
            margin: 20px 0;
            padding: 10px 0;
            color: #232326;
            background: #fff;
            @include borderRadius(40px);
            .app-name {
                padding: 0 20px;
                color: $red;
                font-size: 40px;
                font-weight: bold;
                border-right: 1px solid #666;
            }
            .icon-search {
                padding: 0 20px;
                font-size: 34px;
            }
            .search-title {
                font-size: 24px;
                color: #666;
            }
        }
        .icon-iconyonghu{
            font-size: 44px;
        }
    }

    .swiper-container .swiper_img {
        height: 400px;
    }

    .category-list {
        margin-top: 60px;
        display: flex;
        flex-shrink: 0;
        flex-wrap: wrap;
        width: 100%;
        padding-bottom: 26px;
        div {
            display: flex;
            flex-direction: column;
            width: 20%;
            text-align: center;
            img {
                width: 80px;
                height: 80px;
                margin: 26px auto 16px auto;
            }
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
