$(document).ready(function(){
	required = ["equip_id", "group_name"];
	// errornotice = $("#error");
	// The text to show up within a field when it is incorrect
	emptyerror = "此项不能为空";
	$("#change_entry").submit(function(){
		//Validate required fields
		for (i=0;i<required.length;i++) {
			var input = $('#'+required[i]);
			if ((input.val() == "") || (input.val() == emptyerror)) {
				input.addClass("needsfilled");
				input.parent().parent().addClass('error');
				input.val(emptyerror);
				// errornotice.fadeIn(750);
			} else {
				input.removeClass("needsfilled");
				input.parent().parent().removeClass('error');
			}
		}
		//if any inputs on the page have the class 'needsfilled' the form will not submit
		if ($(":input").hasClass("needsfilled")) {
			return false;
		} else {
			// errornotice.hide();
			return true;
		}
	});
	// Clears any fields in the form when the user clicks on them
	$(":input").focus(function(){
	   if ($(this).hasClass("needsfilled") ) {
			$(this).val("");
			$(this).removeClass("needsfilled");
			$(this).parent().parent().removeClass('error');
	   }
	});
});