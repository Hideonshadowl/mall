<template>
    <div class="shopcart-box">
        <div v-for="item in shopcartlist" style="margin-top: 0.2rem;border-bottom-style: dotted;border-width: 0.01rem">
          <img :src=item[0].img_url alt="" style="height: 40%;width: 40%">
          <span style="font-size: 0.5rem;position: relative;left: 1.2rem;top: -0.25rem;color: red">{{item[0].price*item[1]}}¥</span>
          <span style="font-size: 0.4rem;position: relative;top: -3.5rem"> {{item[0].name}}</span>
          <div class="cart-quantity" style="width: 210px;
                        height: 60px;
                        line-height: 60px;
                        color: #999;
                        background: #fff;">
            <i @click="reduce(item)"  style="width: 60px;
                            height: 100%;
                            text-align: center;
                            line-height: 60px;
                            font-style: normal;
                            font-size: 50px;
                            background: #F7F7F7;">-</i>
            <span>{{item[1]}}</span>
            <i @click="add(item)" style="width: 60px;
                            height: 100%;
                            text-align: center;
                            line-height: 60px;
                            font-style: normal;
                            font-size: 50px;
                            background: #F7F7F7;">+</i>
          </div>
        </div>
      <navBar></navBar>
    </div>
</template>

<script>
    import navBar from '../../components/navBar'
    import {mapState,mapActions} from 'vuex'

    export default {
        computed:mapState(['shopcartlist']),
        data() {
            return {
                changestyle:'',
                imageHost: '',
                cartProductVoList: '',
                recommendList: [],
                cartTotalPrice: 0,
                allChecked: false,
                startX: 0,
                endX: 0,
                deleteProductId: 0,
                popupTitle: '',
                popupShow: false,
                isLoading: true
            }
        },

        created() {

        },
        mounted(){
          console.log(this.shopcartlist)
        },
        methods: {
          ...mapActions(['reducecount','addcount']),
          selectProduct() {
                this.$refs.iii.class='iconfont icon-weibiaoti38';
            },


            reduce(val) {
                console.log('fuck');
                this.reducecount(val);
                this.$forceUpdate();
                console.log('finish');
            },
            add(val) {
                console.log('fuck');
                this.addcount(val);
                this.$forceUpdate();
                console.log('finish');
            },

            },

          components: {
              navBar,
          }
    }
</script>

<style lang="scss" scoped="" type="text/scss">

</style>
