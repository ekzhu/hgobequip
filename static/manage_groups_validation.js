$(document).ready(function(){
	required = ["new_group_name", "group_to_delete"];
	// errornotice = $("#error");
	// The text to show up within a field when it is incorrect
	emptyerror = "此项不能为空";
	$("#manage_group_form").submit(function(){
		//Validate required fields
		for (i=0;i<required.length;i++) {
			var input = $('#'+required[i]);
			if ((input.val() == "") || (input.val() == emptyerror)) {
				input.addClass("needsfilled");
				input.val(emptyerror);
				// errornotice.fadeIn(750);
			} else {
				input.removeClass("needsfilled");
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
	   }
	});
});