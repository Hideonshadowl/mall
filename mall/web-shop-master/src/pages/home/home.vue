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

        <swiper :options="swiperOption" style="margin-top: 0.8rem">
          　　<swiper-slide v-for="(item,index) in swiper_img" :key="index">
          　　　　<img :src='item' alt="" style="height: 5rem;width: 10rem">
          　　</swiper-slide>
          　　<div class="swiper-pagination" slot="pagination"></div>
        </swiper>


        <el-carousel indicator-position="outside">
          <el-carousel-item v-for="item in ['公告1','公告2']" :key="item">
            <h3>{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>


        <div style="display: flex;flex-wrap: wrap;margin-left: 0.4rem" >
          <div style="width: 25%;height: 2.7rem" v-for="item in ['威士忌','琴酒','白兰地','轩尼诗','伏加特','朗姆酒','龙舌兰','金酒']" @click="show">
            <img style="width: 2rem;height: 2rem" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574161425237&di=e28618fc970343d607baaeaf40697078&imgtype=0&src=http%3A%2F%2Fimg1.juimg.com%2F160118%2F330718-16011QRF647.jpg" alt="">
            <p style="font-size: 0.4rem;position: relative;left: -0.25rem;text-align: center">{{item}}</p>
          </div>
        </div>

        <p style="font-size: 0.5rem;margin-left: 4rem;margin-top: 0.2rem;float: left">店长推荐</p>
        <section class="floor-list" style="position: relative;top: 0.5rem">
                <div class="floor-content">
                    <div class="floor-category" v-for="category in floorList" >
                        <div class="floor-products">
                          <img style="width: 3rem;height: 3rem" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574161425237&di=e28618fc970343d607baaeaf40697078&imgtype=0&src=http%3A%2F%2Fimg1.juimg.com%2F160118%2F330718-16011QRF647.jpg" alt="">
                        </div>
                    </div>
                </div>
        </section>

    </div>
</template>

<script>
    import mHeader from 'components/mHeader'
    import navBar from 'components/navBar'
    import slider from 'components/common/slider'
    import {homeData,checkLogin} from "../../service/getData";
    import {getStore,setStore} from "../../common/js/util";
    import Swiper from 'swiper';
    import 'swiper/dist/css/swiper.min.css';
    export default {



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
                swiper_img:['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574161425237&di=e28618fc970343d607baaeaf40697078&imgtype=0&src=http%3A%2F%2Fimg1.juimg.com%2F160118%2F330718-16011QRF647.jpg',
                            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574161425238&di=2a82bd9c3eefc530ac31191d9e2a1813&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Faa3343276cb5726d5c0d802a12d26c57ee92d942bc4e-I41DJj_fw658',
                            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574161425229&di=6c5bfe9a3adeb6a8f86fb7c8b14b3e59&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Fb4b3f04be1818c57efe272e6b23afa895751deab1210c-q25FRJ_fw658',
                            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574161520573&di=c7a24115e8d4823e240ab29e2b96a516&imgtype=0&src=http%3A%2F%2Fpic2.zhimg.com%2Fv2-55f2b35fbb6b572cf9cc1c343ed1a1a0_1200x500.jpg'],
                headList: [],
                categoryList: [],
                floorList: ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a'],
                headerActive: true,
                isLogin: false
            }
        },
        beforeCreate(){

        },
        created(){

        },
        mounted() {

        },
        methods: {
            // pageScroll() {
            //     let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
            //     scrollTop > 100 ? this.headerActive = true : this.headerActive = true
            // },
            show(){
                this.$router.push('./product-list')
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
