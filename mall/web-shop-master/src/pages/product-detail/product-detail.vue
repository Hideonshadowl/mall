<template>
    <div class="product-detail">
        <header class="detail-nav">
            <i class="iconfont icon-left" @click="goBack"></i>
            <div class="nav-list">

                <!--<span data-type="detail" @click="scrollToView($event)" :class="{'active' : navIndex === 1}">-->
                    <!--<i class="iconfont icon-location" v-show="navIndex === 1"></i>商品详情-->
                <!--</span>-->
                <!--<span data-type="recommend" @click="scrollToView($event)" :class="{'active' : navIndex === 2}">-->
                    <!--<i class="iconfont icon-location" v-show="navIndex === 2"></i>商品推荐-->
                <!--</span>-->
            </div>
            <i class="iconfont icon-More"></i>
        </header>
        <section class="product-focus">
          <img :src=this.good.img_url alt="" style="width: 10rem;height: 9rem">
        </section>
        <span :class="{'active' : navIndex === 0}" data-type="product" @click="scrollToView($event)" style="">
                 <span style="margin-left: 0.4rem;font-size: 0.5rem">{{this.good.name}}</span>
                 <span style="margin-left: 0.4rem;font-size: 0.5rem">{{this.good.volume}}ml</span>
                 <span style="margin-left: 0.4rem;font-size: 0.5rem">{{this.good.degree}}vol</span>
                 <p style="margin-left: 0.4rem;font-size: 0.5rem;color: red">{{this.good.price}}¥</p>
        </span>
        <section class="detail-info">
            <p class="detail-info-name" v-text="productData.name"></p>
            <p class="detail-info-subtitle" v-text="productData.subtitle"></p>
            <div>
                <span class="detail-info-stock" v-text="`销量:90`" style="margin-top: -0.25rem"></span>
            </div>
        </section>
        <section>
            <div class="detail-content" ref="detailContent" id="content">
                <p class="detail-gap"></p>
                <ul>
                    <!--<li @click="show1">概述</li>-->
                    <!--<li @click="show2">参数</li>-->
                    <!--<li @click="show3">安装服务</li>-->
                    <!--<li @click="show4">常见问题</li>-->
                </ul>
                <div><p style="border-style:solid;font-size: 0.5rem;border-radius: 0.2rem;width: 4rem;margin-top: 0.5rem">配送范围</p></div>
                <div><p style="border-style:solid;font-size: 0.5rem;border-radius: 0.2rem;width: 4rem;margin-top: 0.5rem">发货时间</p></div>
            </div>
            <div  style="width: 100%;background: #eee;height: 0.25rem;margin-top: 1.2rem"></div>
            <img src="../../assets/product.gif" alt="" style="width: 10rem;height: 9rem">
            <img src="../../assets/order.gif" alt="" style="width: 10rem;height: 9rem;margin-top: 0.4rem">



            <div ref="detailRecommend" id="recommend">
            </div>
            <div class="detail-cart">
                <div class="detail-cart-left">
                    <div class="like">
                        <i @click="lightLove" v-if="!isLoved" class="iconfont icon-lovetaoxin"></i>
                        <i @click="cancelLove" v-else class="iconfont icon-love"></i>
                        <span>喜欢</span>
                    </div>
                    <router-link tag="div" to="/shopcart" class="cart">
                        <i class="iconfont icon-gouwuche"></i>
                        <span>购物车</span>
                        <span class="cart-num" v-text="cartCount" v-show="cartCount"></span>
                    </router-link>
                </div>
                <div class="detail-cart-right">
                    <button @click="addCart">加入购物车</button>
                    <button @click="$router.push('./order')">立即购买</button>
                </div>
            </div>
        </section>
        <transition name="fade">
            <div class="modal" @click="closeCart" v-show="cartShow"></div>
        </transition>
        <transition name="slide-up">
            <section class="cart-wrap" v-show="cartShow">
                <div class="cart-content">
                    <div class="cart-head">
                        <img :src=this.good.img_url v-if="subImageList.length > 0">
                        <div>
                            <span class="price">{{this.good.price*this.productCount}}¥</span>
                            <p>{{productData.name}}</p>
                        </div>
                        <!--<i class="iconfont icon-close" @click="closeCart"></i>-->
                    </div>
                    <!--<div class="cart-config">-->
                        <!--<div class="subtitle">-->
                            <!--<span>商品介绍</span>-->
                            <!--<span>{{productData.subtitle}}</span>-->
                        <!--</div>-->
                    <!--</div>-->
                    <div class="cart-count">
                        <span>数量</span>
                        <div class="cart-quantity">
                            <i @click="reduceCount" :class="{'active' : productCount === 1}">-</i>
                            <span>{{productCount}}</span>
                            <i @click="addCount" :class="{'active' : productCount === productData.stock}">+</i>
                        </div>
                    </div>
                    <button class="add-cart" @click="confirmCart()">确认</button>
                </div>
            </section>
        </transition>
        <!--<framework v-show="frameShow"></framework>-->
    </div>
</template>

<script>
    import framework from 'components/common/frame'
    import slider from 'components/common/slider'
    import {productDetail, cartCount, addCart} from "../../service/getData";
    import {mapState,mapActions} from 'vuex'

    export default {
        data() {
            return {
                good:'',
                good_Introduction:true,
                good_parameter:false,
                good_service:false,
                good_problem:false,
                subImageList: ['../../assets/banner1.jpg',],
                productData: {},
                productCount:1,
                cartCount: 0,
                navIndex: 0,    //导航索引
                isLoved: false,
                cartShow: false,
                frameShow: true
            }
        },
        computed:mapState(['shopcartlist']),

        created() {
            this.good=this.$route.query.good
        },
        mounted() {

        },
        methods: {
            ...mapActions([
                'addshoplist','clearshoplist'
            ]),
          show1(){this.good_Introduction=true; this.good_parameter=false;this.good_service=false;this.good_problem=false},
          show2(){this.good_Introduction=false;this.good_parameter=true;this.good_service=false;this.good_problem=false},
          show3(){this.good_Introduction=false;this.good_parameter=false;this.good_service=true;this.good_problem=false},
          show4(){this.good_Introduction=false;this.good_parameter=false;this.good_service=false;this.good_problem=true},
            //商品详情
            async getDetail() {
                let subImages = [],
                    imageHost = ''
                await productDetail(this.$route.params.id).then((res) => {
                    console.log(res)
                    subImages = res.data.subImages.split(',')
                    imageHost = res.data.imageHost
                    this.productData = res.data
                })
                subImages.forEach((item) => {
                    this.subImageList.push({
                        imgUrl: imageHost + item
                    })
                })
            },
            getCartCount() {
                cartCount().then((res) => {
                    // console.log(res)
                    this.cartCount = res.data
                })
            },
            addCart() {
                this.cartShow = true

            },
            addCount(){
                if(this.productCount === this.productData.stock){
                    return
                }
                this.productCount ++

            },
            reduceCount(){
                if(this.productCount === 1){
                    return
                }
                this.productCount --
            },
            //加入购物车
            confirmCart(){
                this.addtest(this.good,this.productCount);
                this.cartShow=false;
                alert('添加成功');
                // this.clearshoplist();
                console.log(this.shopcartlist)

            },
            addtest(obj,amount){
              this.addshoplist([obj,amount])
            },
            closeCart() {
                this.cartShow = false
                ModalHelper.beforeClose()
            },
            scrollToView(e) {
                let $type = e.target.getAttribute('data-type')
                switch ($type) {
                    case 'product':
                        this.navIndex = 0
                        break
                    case 'detail':
                        this.navIndex = 1
                        break
                    case 'recommend':
                        this.navIndex = 2
                        break
                }
                document.documentElement.scrollTop = document.querySelector('#content').offsetTop
                // console.log($type)
                // console.log(document.querySelector('#content').offsetTop)
                // console.log(document.querySelector('#recommend').offsetTop)
            },
            //监听页面滚动
            pageScroll() {
                // let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop

            },
            //喜欢
            lightLove() {
                this.isLoved = true
                this.followList.unshift(this.productData)
                this.ADD_FOLLOW(this.followList)
            },
            //取消喜欢
            cancelLove() {
                this.isLoved = false
                this.REDUCE_FOLLOW('reduce', this.productData.id)
            },
            goBack() {
                this.$router.go(-1)
            }
        },
        components: {
            framework,
            slider
        },
    }
</script>

<style lang="scss" type="text/scss">
    @import '../../common/style/mixin';

    .product-detail {
        width: 100%;
        &.active {
            background: rgba(0, 0, 0, .6);
        }
        .detail-nav {
            @include fj;
            position: fixed;
            left: 0;
            top: 0;
            width: 100%;
            height: 88px;
            padding: 0 20px;
            line-height: 88px;
            box-sizing: border-box;
            z-index: 1000;
            color: #252525;
            background: #fff;
            border-bottom: 1px solid #dcdcdc;
            i {
                font-size: 50px;
                color: #000;
            }
            div span {
                padding: 0 20px;
                font-size: 28px;
                &.active {
                    color: $red;
                }
                .iconfont {
                    padding-right: 8px;
                    font-size: 28px;
                    color: $red;
                }
            }
        }
        .detail-slider img {
            height: 700px;
        }
        .product-focus {
            margin-top: 88px;
        }
        .detail-info {
            width: 100%;
            padding: 20px 30px;
            font-size: 30px;
            box-sizing: border-box;
            .detail-info-name {
                font-size: 40px;
                color: #333;
            }
            .detail-info-subtitle {
                padding: 10px 0;
                font-size: 28px;
                color: #999;
            }
            div {
                @include fj;
                padding: 10px 0;
                font-size: 32px;
                color: #999;
                .detail-info-price {
                    color: $red;
                    font-size: 44px;
                }
            }
        }
        .detail-content {
            width: 100%;
            .detail-gap {
                width: 100%;
                height: 20px;
                background: #eee;
            }
            ul {
                @include fj;
                width: 100%;
                margin: 20px 0;
                li {
                    flex: 1;
                    padding: 10px 0;
                    text-align: center;
                    font-size: 30px;
                    border-right: 1px solid #999;
                    box-sizing: border-box;
                    &:last-child {
                        border-right: none;
                    }
                }
            }
            div {
                width: 100%;
                overflow: hidden;
                p {
                    width: 100%;
                    font-size: 40px;
                    text-align: center;
                }
                img {
                    width: 100%;
                }
            }
        }
        .detail-cart {
            @include fj;
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 100px;
            line-height: 100px;
            font-size: 30px;
            background: #FEFBF9;
            z-index: 1000;
            transform: translateZ(0);
            -webkit-transform: translateZ(0);
            @include boxSizing;
            .detail-cart-left {
                @include fj;
                width: 46%;
                padding: 0 30px;
                @include boxSizing;
                .like {
                    width: 40%;
                    display: flex;
                    flex-direction: column;
                    text-align: center;
                    .iconfont {
                        font-size: 34px;
                        line-height: 60px;
                        color: #000000;
                        font-weight: bold;
                        &.icon-love {
                            color: $red;
                        }
                    }
                    span {
                        line-height: 30px;
                        font-size: 26px;
                    }
                }
                .cart {
                    @extend .like;
                    position: relative;
                    .cart-num {
                        position: absolute;
                        right: 20px;
                        top: 0;
                        width: 30px;
                        height: 30px;
                        text-align: center;
                        line-height: 30px;
                        color: #fff;
                        font-size: 22px;
                        background: $red;
                        @include borderRadius(50%);
                    }
                    .iconfont {
                        font-size: 40px;
                        font-weight: normal;
                    }
                }
            }
            .detail-cart-right {
                width: 50%;
                button {
                    width: 50%;
                    height: 100px;
                    color: #fff;
                    font-size: 30px;
                    background: rgba(246,53,21,.9);
                    &:nth-child(1) {
                        margin-right: -10px;
                        background: rgba(246,53,21,.9);
                    }
                }
            }
        }
        .modal{
            position: fixed;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            z-index: 1000;
            background: rgba(0,0,0,.6);
        }
        .cart-wrap {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 60%;
            z-index: 99999999;
            .cart-content {
                position: absolute;
                left: 0;
                bottom: 0;
                width: 100%;
                height: 100%;
                font-size: 30px;
                background: #fff;
                .cart-head {
                    display: flex;
                    width: 100%;
                    padding: 30px;
                    @include boxSizing;
                    img {
                        width: 180px;
                        height: 180px;
                        margin-top: -60px;
                        border: 1px solid #999;
                    }
                    div {
                        display: flex;
                        flex-direction: column;
                        justify-content: space-between;
                        width: 64%;
                        margin-left: 20px;
                        .price {
                            display: block;
                            font-size: 34px;
                            color: $red;
                            padding-bottom: 10px;
                        }
                        p {
                            max-height: 40px;
                            overflow: hidden;
                        }
                    }
                    .iconfont {
                        position: absolute;
                        top: 30px;
                        right: 30px;
                        font-size: 28px;
                        color: #dcdcdc;
                    }
                }
                .cart-config {
                    @extend .cart-head;
                    padding: 0 30px 30px 30px;
                    .subtitle {
                        width: 100%;
                        margin-left: 0;
                        padding: 20px 0;
                        span {
                            &:first-child {
                                color: #999;
                                padding-bottom: 20px;
                            }
                        }
                    }
                }
                .cart-count {
                    @include fj;
                    width: 100%;
                    padding: 0 30px 30px 30px;
                    @include boxSizing;
                    .cart-quantity {
                        @include fj;
                        width: 210px;
                        height: 60px;
                        line-height: 60px;
                        color: #999;
                        background: #fff;
                        span {
                            width: 80px;
                            height: 100%;
                            text-align: center;
                            line-height: 60px;
                            background: #F7F7F7;
                        }
                        i {
                            width: 60px;
                            height: 100%;
                            text-align: center;
                            line-height: 60px;
                            font-style: normal;
                            font-size: 50px;
                            background: #F7F7F7;
                            &.active {
                                color: #dcdcdc;
                            }
                        }
                    }
                }
                .add-cart {
                    position: absolute;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    height: 100px;
                    text-align: center;
                    line-height: 100px;
                    color: #fff;
                    font-size: 30px;
                    background: $red;
                }
            }
        }
        .slide-up-enter-active, .slide-up-leave-active {
            transition: all 0.5s;
        }
        .slide-up-enter, .slide-up-leave-to {
            transform: translate3d(0, 100%, 0);
        }
    }
</style>
