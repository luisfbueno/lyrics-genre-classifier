var app = new Vue({
  el: '#app',
  data: {
    lyrics: 'Vai tua vida\nTeu caminho é de paz e amor\nA tua vida\nÉ uma linda canção de amor\nAbre os teus braços e canta\nA última esperança\nA esperança divina\nDe amar em paz',
    genero: '',
    url_destino: 'http://127.0.0.1:5000/'
  },
  methods: {
    request: function() {
      var self=this;
      var str = this.lyrics;
      var json = {"Lyrics": str}
      json = JSON.stringify(json)
      console.log(json)

      this.$http.post(url_destino,json).then(function(response){
        if(response.status == "200"){
            console.log(response.data[0]);
          resp = response.data[0]
          if(resp == 0){
            self.genero = 'Bossa Nova'
          }
          else if(resp == 1){
            self.genero = 'Funk'
          }
          else if(resp == 2){
            self.genero = 'Gospel'
          }
          else if(resp == 3){
            self.genero = 'Sertanejo'
          }
          else{
            self.genero = ''
          }

        }
      })
    }
  }
})
