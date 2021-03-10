$(document).ready(function(){


	var txt1 = "<option value='ferrari'>Tokyo Ghoul				</option>";        
	var txt2 = "<option value='mclaren'>Tokyo Ghoul					</option>" ; 
	var txt3 = "<option value='bugatti'>Death Note				</option>" ; 
	var txt4 = "<option value='lamborgini'>Dragon Ball Z		</option>" ; 
	var txt5 = "<option value='pagani'>Shingeki No kiyojin		</option>" ; 
	
	$("select").append(txt1, txt2,txt3,txt4,txt5);  		//dropdown list  using jquery

/*	
	$("div").append("<button onclick='myFunction()' class='dropbtn'>Dropdown</button>");
	$("div").append( "<div id='myDropdown' class='dropdown-content'>");
	$("div").append( "<a href='#'>Tokyo Ghoul		</a>");
	$("div").append("<br>");
	$("div").append( "<a href='#'>Tokyo Ghoul		</a>");
	$("div").append("<br>");
	$("div").append( "<a href='#'>Death Note	</a>");
    $("div").append("<br>");
	$("div").append( "<a href='#'>Dragon Ball Z	</a>");
	$("div").append("<br>");
	$("div").append( "<a href='#'>Shingeki No kiyojin</a>");
	$("div").append( "</div>");
	

	$("a").hide();
	
	$("#dropdown").click(function(){
		$("a").slideToggle();
	});
*/
	var i=0;
	while(i<100000)
	{
		$("#blink").fadeToggle();
		i=i+1;
	}

	$("#bgbtn").click(function(){
	   $("body").css("background-image","url('tokyo1.jpg')");
	   //$("body").css("background-repeat","no-repeat");   
	});
	
	$(document).on("keypress", "input", function(e){
			if(e.which == 51){
				alert("You pressed 3");
			}
	});
    	
	
});
