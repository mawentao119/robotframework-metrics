from bs4 import BeautifulSoup
import sys
import os
from robot.api import ExecutionResult, ResultVisitor

"""
@Author: Software tester with minimal coding knowledge.
Suggest or provide feedback to improve coding standard and style
Thanks in advance :)
"""

# Get report result - OS independent
current_path = os.getcwd()
# output.xml file location
text_file = os.path.join(os.path.curdir, 'output.xml')
# performance report result file location
result_file = os.path.join(os.path.curdir, 'rf_metrics_result.html')

result = ExecutionResult(text_file)
result.configure(stat_config={'suite_stat_level': 2,
                              'tag_stat_combine': 'tagANDanother'})

head_content = """

<!DOCTYPE html>
<html>
<title>RF Metrics Report</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap.min.css" rel="stylesheet" type="text/css"/>
<script src="https://code.jquery.com/jquery-3.3.1.js" type="text/javascript"></script>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js" type="text/javascript"></script>
<script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap.min.js" type="text/javascript"></script>
   
<style>
//body, h1,h2,h3,h4,h5,h6 {font-family: "Montserrat", sans-serif}
.w3-row-padding img {margin-bottom: 12px}

/* Set the width of the sidebar to 120px */
.w3-sidebar {width: 120px;background: #222;}

/* Add a left margin to the "page content" that matches the width of the sidebar (120px) */
#main {margin-left: 120px}

/* Remove margins from "page content" on small screens */
@media only screen and (max-width: 600px) {#main {margin-left: 0}}

* {box-sizing: border-box}

/* Set height of body and the document to 100% */
body, html {
    height: 100%;
    margin: 0;
    font-family:  Comic Sans MS;
}

/* Style tab links */
.tablink {
    color: white;
    cursor: pointer;
}

.tablink:hover {
    background-color: #777;
}

.loader,
.loader:after {
    border-radius: 50%;
    width: 10em;
    height: 10em;
    position: center;
}
.loader {
    margin: 60px auto;
    font-size: 10px;
    position: relative;
    text-indent: -9999em;
    border-top: 1.1em solid rgba(255, 255, 255, 0.2);
    border-right: 1.1em solid rgba(255, 255, 255, 0.2);
    border-bottom: 1.1em solid rgba(255, 255, 255, 0.2);
    border-left: 1.1em solid #ffffff;
    -webkit-transform: translateZ(0);
    -ms-transform: translateZ(0);
    transform: translateZ(0);
    -webkit-animation: load8 1.1s infinite linear;
    animation: load8 1.1s infinite linear;
}
@-webkit-keyframes load8 {
    0% {
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
    }
    100% {
        -webkit-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}
@keyframes load8 {
    0% {
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
    }
    100% {
        -webkit-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}
#loadingDiv {
    position:absolute;;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background-color:grey;
}

#dashboard {background-color: white;}
#testMetrics {background-color: white;}
#keywordMetrics {background-color: white;}

</style>
</head>
</html>
"""

soup = BeautifulSoup(head_content,"html.parser")

body = soup.new_tag('body',style="padding: 5px")
soup.insert(20, body)

loadingDiv = soup.new_tag('div')
loadingDiv["id"] = "loadingDiv"
body.insert(1, loadingDiv)

spiner = soup.new_tag('div')
spiner["class"] = "loader"
loadingDiv.insert(0, spiner)

icons_txt= """

<!-- Icon Bar (Sidebar - hidden on small screens) -->
<nav class="w3-sidebar w3-bar-block w3-small w3-hide-small w3-center">
  <a href="#" id="defaultOpen" onclick="openPage('dashboard', this, 'orange')" class="tablink w3-bar-item w3-button w3-padding-large">
    <i class="fa fa-dashboard w3-xxlarge"></i>
    <p>DASHBOARD</p>
  </a>
  <a href="#" onclick="openPage('testMetrics', this, 'orange');executeDataTable('#tm',4)" class="tablink w3-bar-item w3-button w3-padding-large">
    <i class="fa fa-table w3-xxlarge"></i>
    <p>TEST METRICS</p>
  </a>
  <a href="#" onclick="openPage('keywordMetrics', this, 'orange');executeDataTable('#km',5)" class="tablink w3-bar-item w3-button w3-padding-large">
    <i class="fa fa-table w3-xxlarge"></i>
    <p>KEYWORD METRICS</p>
  </a>
</nav>

<!-- Navbar on small screens (Hidden on medium and large screens) -->
<div class="w3-top w3-hide-large w3-hide-medium" id="myNavbar">
  <div class="w3-bar w3-black w3-opacity w3-hover-opacity-off w3-center w3-small">
    <a href="#" id="defaultOpen" onclick="openPage('dashboard', this, 'orange')" class="tablink w3-bar-item w3-button" style="width:25% !important">DASHBOARD</a>
    <a href="#" onclick="openPage('testMetrics', this, 'orange');executeDataTable('#tm',4)" class="tablink w3-bar-item w3-button" style="width:25% !important">TEST METRICS</a>
    <a href="#" onclick="openPage('keywordMetrics', this, 'orange');executeDataTable('#km',5)" class="tablink w3-bar-item w3-button" style="width:25% !important">KEYWORD METRICS</a>
  </div>
</div>

"""

body.append(BeautifulSoup(icons_txt, 'html.parser'))


page_content_div = soup.new_tag('div')
page_content_div["id"] = "main"
page_content_div["class"] = "w3-padding-large"
body.insert(30, page_content_div)

# Tests div
tm_div = soup.new_tag('div')
tm_div["id"] = "testMetrics"
tm_div["class"] = "tabcontent"
page_content_div.insert(50, tm_div)

# Keywords div
km_div = soup.new_tag('div')
km_div["id"] = "keywordMetrics"
km_div["class"] = "tabcontent"
page_content_div.insert(100, km_div)

### ============================ START OF DASHBOARD ======================================= ####

dashboard_content="""
<div class="tabcontent" id="dashboard">
    <h3><b><i class="fa fa-dashboard"></i> Dashboard</b></h3>
  <hr>
  
    <div class="col-md-5 chart-blo-1" id="testChartID" style="height: 350px;"></div>
    <div class="col-md-7 chart-blo-1" id="testsBarID" style="height: 350px;"></div>
    <div class="col-md-5 chart-blo-1" id="keywordChartID" style="height: 350px;"></div>
    <div class="col-md-7 chart-blo-1" id="keywordsBarID" style="height: 350px;"></div>
   
   <script>
    window.onload = function(){
    executeDataTable('#tm',4);
    executeDataTable('#km',5);
    createPieChart('#tm',1,'testChartID','Tests Status:');		
    createBarGraph('#tm',0,4,10,'testsBarID','Top 10 Tests Performance:');
    createPieChart('#km',2,'keywordChartID','Keywords Status:');		
    createBarGraph('#km',1,5,10,'keywordsBarID','Top 10 Keywords Performance:')
	};
   </script>
  </div>
"""
page_content_div.append(BeautifulSoup(dashboard_content, 'html.parser'))

### ============================ END OF DASHBOARD ============================================ ####


### ============================ START OF TEST METRICS ======================================= ####

test_icon_txt="""
<h3><b><i class="fa fa-table"></i> Test Metrics</b></h3>
  <hr>
"""
tm_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))

# Create table tag
table = soup.new_tag('table',style="padding: 5px;")
table["id"] = "tm"
table["class"] = "table table-striped table-bordered"
tm_div.insert(2, table)

thead = soup.new_tag('thead')
table.insert(0, thead)

tr = soup.new_tag('tr')
thead.insert(0, tr)

th = soup.new_tag('th')
th.string = "Test Case"
tr.insert(0, th)

th = soup.new_tag('th')
th.string = "Status"
tr.insert(1, th)

th = soup.new_tag('th')
th.string = "Start Time"
tr.insert(2, th)

th = soup.new_tag('th')
th.string = "End time"
tr.insert(3, th)

th = soup.new_tag('th')
th.string = "Elapsed Time(s)"
tr.insert(4, th)

tbody = soup.new_tag('tbody')
table.insert(11, tbody)

### =============== GET TEST METRICS =============== ###

class TestCaseResults(ResultVisitor):

    def visit_test(self, test):

        table_tr = soup.new_tag('tr')
        tbody.insert(0, table_tr)

        table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 300px; white-space: normal")
        table_td.string = str(test)
        table_tr.insert(0, table_td)

        table_td = soup.new_tag('td')
        table_td.string = str(test.status)
        table_tr.insert(1, table_td)

        table_td = soup.new_tag('td')
        table_td.string = str(test.starttime)
        table_tr.insert(2, table_td)

        table_td = soup.new_tag('td')
        table_td.string = str(test.endtime)
        table_tr.insert(3, table_td)

        table_td = soup.new_tag('td')
        table_td.string = str(test.elapsedtime/float(1000))
        table_tr.insert(4, table_td)

result.visit(TestCaseResults())
### ============================ END OF TEST METRICS ============================================ ####

### ============================ START OF KEYWORD METRICS ======================================= ####

keyword_icon_txt="""
<h3><b><i class="fa fa-table"></i> Keyword Metrics</b></h3>
  <hr>
"""
km_div.append(BeautifulSoup(keyword_icon_txt, 'html.parser'))

# Create table tag
# <table id="myTable">
table = soup.new_tag('table',style="padding: 5px;")
table["id"] = "km"
table["class"] = "table table-striped table-bordered"
km_div.insert(2, table)

thead = soup.new_tag('thead')
table.insert(0, thead)

tr = soup.new_tag('tr')
thead.insert(0, tr)

th = soup.new_tag('th')
th.string = "Test Case"
tr.insert(1, th)

th = soup.new_tag('th')
th.string = "Keyword"
tr.insert(1, th)

th = soup.new_tag('th')
th.string = "Status"
tr.insert(2, th)

th = soup.new_tag('th')
th.string = "Start Time"
tr.insert(3, th)

th = soup.new_tag('th')
th.string = "End time"
tr.insert(4, th)

th = soup.new_tag('th')
th.string = "Elapsed Time(s)"
tr.insert(5, th)

tbody = soup.new_tag('tbody')
table.insert(1, tbody)

class KeywordResults(ResultVisitor):

    def visit_keyword(self,kw):

        table_tr = soup.new_tag('tr')
        tbody.insert(1, table_tr)

        table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 300px; white-space: normal")
        table_td.string = str(kw.parent)
        table_tr.insert(0, table_td)

        table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 300px; white-space: normal")
        table_td.string = str(kw.kwname)
        table_tr.insert(1, table_td)

        table_td = soup.new_tag('td')
        table_td.string = str(kw.status)
        table_tr.insert(2, table_td)

        table_td = soup.new_tag('td')
        table_td.string = str(kw.starttime)
        table_tr.insert(3, table_td)

        table_td = soup.new_tag('td')
        table_td.string = str(kw.endtime)
        table_tr.insert(4, table_td)

        table_td = soup.new_tag('td')
        table_td.string =str(kw.elapsedtime/float(1000))
        table_tr.insert(5, table_td)

result.visit(KeywordResults())
### ============================ END OF KEYWORD METRICS ======================================= ####

script_text="""
 <script>
  function createPieChart(tableID,status_column,ChartID,ChartName){

var chart = new CanvasJS.Chart(ChartID,{  
    exportFileName: ChartName,
	exportEnabled: true,	
    animationEnabled: true,
	title: {
    text: ChartName,
    fontFamily: "Comic Sans MS",
    fontSize: 15,
	horizontalAlign: "left",
    fontWeight: "bold"
    
  },
  data: []
  
});

var rows = $(tableID).dataTable().fnGetNodes();
var columns;
var isPass = 0;
var isFail = 0;

for (var i = 0; i < rows.length; i++) {
  columns = $(rows[i]).find('td');  
  
    if (columns[Number(status_column)].innerHTML.trim() == "PASS") {
      isPass = isPass + 1;      
    } else {
      isFail = isFail + 1;      
    }
  }  
var status = [{label:'PASS',y:parseInt(isPass),color:"Green"},{label:'FAIL',y:parseInt(isFail),color:"Red"}];
  chart.options.data.push({
    //type: "pie",
    type: "doughnut",
    startAngle: 60,
    //innerRadius: 60,
    indexLabelFontSize: 15,
    indexLabel: "{label} - #percent%",
    toolTipContent: "<b>{label}:</b> {y} (#percent%)",

    //name: ($(columns[0]).html()), 
    //showInLegend: true,
    //legendText: ($(columns[0]).html()),
    dataPoints: status
  });
  chart.render();
}
 </script>
 <script>
  function createBarGraph(tableID,keyword_column,time_column,limit,ChartID,ChartName){
      var chart = new CanvasJS.Chart(ChartID, {
       exportFileName: ChartName,
        exportEnabled: true,	
        animationEnabled: true,
    title: {
        text: ChartName,
        fontFamily: "Comic Sans MS",
        fontSize: 15,
        textAlign: "centre",
        dockInsidePlotArea: true,
        fontWeight: "bold"
    },
      axisX:{
        //title:"Axis X title",
        labelAngle: 0,
        labelFontSize: 10,
        labelFontFamily:"Comic Sans MS",
        
      },
      axisY:{
        title:"Seconds (s)",
      },
      data: []
    });

var status = [];
css_selector_locator = tableID + ' tbody >tr'
var rows = $(css_selector_locator);
var columns;

for (var i = 0; i < rows.length; i++) {
    if (i == Number(limit)){
        break;
    }
	//status = [];
    name_value = $(rows[i]).find('td'); 
  
    time=($(name_value[Number(time_column)]).html()).trim();
	status.push({label:$(name_value[Number(keyword_column)]).html(),y:parseFloat(time)});
  }  
	chart.options.data.push({
    type: "column",
    indexLabel: "{y} s",
    toolTipContent: "<b>{label}:</b> {y} s",
    dataPoints: status
  });
  
    chart.render();
	}
  </script>
 </script>
 <script>
  function executeDataTable(tabname,sortCol) {
    $(tabname).DataTable(
        {
        retrieve: true,
        "order": [[ Number(sortCol), "desc" ]]
        } 
    );
}
 </script>
 <script>
  function openPage(pageName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.style.backgroundColor = color;

}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
 </script>
 <script>
  //$('body').append('<div style="" id="loadingDiv"><div class="loader"></div></div>');
$(window).on('load', function(){
  setTimeout(removeLoader, 0); //wait for page load PLUS zero seconds.
});
function removeLoader(){
    $( "#loadingDiv" ).fadeOut(50, function() {
      // fadeOut complete. Remove the loading div
      $( "#loadingDiv" ).remove(); //makes page more lightweight
  });
}
</script>
"""

body.append(BeautifulSoup(script_text, 'html.parser'))

### ====== WRITE TO RF_METRICS_REPORT.HTML ===== ###

# Write output as html file
with open(result_file, 'w') as outfile:
    outfile.write(soup.prettify())