//Javascript functions//
//Can be called within any html page that this script has been attached to//

//Back a page function//
function Previous_Page
{
<FORM>
<INPUT TYPE="Button" VALUE="Previous Page" onClick="history.go(-1)">
</FORM>
}//Entered this in html page prices.html we can reuse this code on any page on the website//


function Specify_Referring_Page
{
var allowedreferrer = "http://www.webair.com/admin_editpage"; 
	if (document.referrer.indexOf(allowedreferrer) == -1) 
	{
	alert("You can only access this page from " + allowedreferrer);
	window.location=allowedreferrer;
	}
}
//Stops users from being able to type the correct address into the url & access pages that aren't supposed to be accesible//

function Calculation_placeholder(a, b)//Verible placeholders//
{
	return a + b;
	//This function could be used to add up totals & calculate tax//
}

function Showdate //Used to show date in this format Day, Month 20, year//
{
var now = new Date();
var days = new Array('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');
var months = new Array('January','February','March','April','May','June','July','August','September','October','November','December');
var date = ((now.getDate()<10) ? "0" : "")+ now.getDate();
function fourdigits(number)	{
	return (number < 1000) ? number + 1900 : number;
								}
today =  days[now.getDay()] + ", " +
         months[now.getMonth()] + " " +
         date + ", " +
         (fourdigits(now.getYear())) ;
document.write(today);
}
