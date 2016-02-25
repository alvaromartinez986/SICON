/**
 * Created by nelson on 25/02/16.
 */
$.ajax({
    success: function(data) {
        console.log(data);
    },
    failure: function(data) {
        alert('Got an error dude');
    }
});