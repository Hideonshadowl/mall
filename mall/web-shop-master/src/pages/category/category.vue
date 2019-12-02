<template>
    <div style="">
        <div >
            <header class="category-header wrap">
                <i class="iconfont icon-left" @click="goHome"></i>
                <div class="header-search">
                    <i class="iconfont icon-search"></i>
                    <router-link tag="span" class="search-title" to="./search">家电返场同价11.11</router-link>
                </div>
                <i class="iconfont icon-More"></i>
            </header>
            <nav-bar></nav-bar>

            <div style="margin-top: 2rem;margin-bottom: 2rem">
            <div style="box-shadow: 0 0.2rem 0.4rem rgba(0, 0, 0, .12), 0 0 0.6rem rgba(0, 0, 0, .04);border-radius: 0.3rem;
                        margin-top: 1rem;margin-left:0.75rem;width: 85%;height: 5rem" v-for="a in ['a','a','a','a','a','a']">
              <p style="font-size: 0.5rem;margin-left: 0.4rem;margin-top: 0.5rem">分类一</p>
              <div style="display: flex;flex-wrap: wrap;margin-top: 0.1rem">
                <p style="width: 30%;font-size: 0.4rem;margin-top: 0.6rem;margin-left:1.1rem;background-color: blanchedalmond" v-for="b in ['a','a','a','a','a','a']">二级分类</p>
              </div>
            </div>
            </div>


        </div>
    </div>
</template>

<script>
    import mHeader from '../../components/mHeader'
    import navBar from '../../components/navBar'
    import listScroll from '../../components/common/list-scroll'
    import {categoryData} from "../../service/getData";

    export default {
        components: {
            mHeader,
            navBar,
            listScroll
        },
        data() {
            return {
                categoryData: [],
                currentIndex: 0
            }
        },
        created() {
            window.addEventListener('scroll', this.pageScroll)
            console.log('我是父路由')
            this.getCategoryData()
        },
        mounted() {
            this.setSearchWrapHeight()
        },
        methods: {
            //获取catgory菜单数据
            async getCategoryData() {
                await categoryData().then((res) => {
                  console.log(res)
                    this.categoryData = res.data
                })
            },
            //动态设置searc-wrap的高
            setSearchWrapHeight() {
                let $screenHeight = document.documentElement.clientHeight
                this.$refs.searchWrap.style.height = $screenHeight - 200 + 'px'
            },
            //左侧菜单和右侧区域联动
            selectMenu($index) {
                this.currentIndex = $index
            },
            selectProduct(title){
                this.$router.push('./product-list?keyword='+title)
            },
            goHome(){
              console.log(11111)
              this.$router.push('/home')
            }
        }
    }
</script>

<style lang="scss" scoped="" type="text/scss">
    @import '../../common/style/mixin';

    .category-header {
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
        color: #656771;
        z-index: 10000;
        &.active {
            background: $red;
        }
        .icon-left {
            font-size: 50px;
            font-weight: bold;
        }
        .header-search {
            display: flex;
            width: 80%;
            height: 40px;
            line-height: 40px;
            margin: 20px 0;
            padding: 10px 0;
            color: #232326;
            background: #F7F7F7;
            @include borderRadius(40px);
            .icon-search {
                padding: 0 20px 0 40px;
                font-size: 34px;
            }
            .search-title {
                font-size: 24px;
                color: #666;
            }
        }

    }


</style>
