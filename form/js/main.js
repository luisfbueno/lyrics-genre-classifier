var app = new Vue({
  el: '#app',
  data: {
    lyrics: 'Vai tua vida\nTeu caminho é de paz e amor\nA tua vida\nÉ uma linda canção de amor\nAbre os teus braços e canta\nA última esperança\nA esperança divina\nDe amar em paz',
    genero: ''
  },
  methods: {
    request: function() {
      var self=this;
      var str = this.lyrics;
      var json = {"Lyrics": str}
      json = JSON.stringify(json)
      console.log(json)

      this.$http.post('http://127.0.0.1:5000/',json).then(function(response){
        if(response.status == "200"){
            console.log(response.data[0]);
        self.genero = response.data // use self instead of this
        }
      })
    }
  }
})
