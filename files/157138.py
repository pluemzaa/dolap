<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work_flowforithm_1"/>
        <attribute name="authors" value="Vivobook"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:06:56 PM"/>
        <attribute name="created" value="Vml2b2Jvb2s7TEFQVE9QLTFEODVNVU02OzI1NjgtMDctMTY7MDU6NTI6NTYgUE07MzE3Nw=="/>
        <attribute name="edited" value="Vml2b2Jvb2s7TEFQVE9QLTFEODVNVU02OzI1NjgtMDctMTY7MDY6MDY6NTYgUE07MTszMjg1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <declare name="Child, Adult, total" type="Integer" array="False" size=""/>
            <assign variable="Child" expression="120"/>
            <assign variable="Adult" expression="189"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="Child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="Adult"/>
            <assign variable="total" expression="(Child * 120) + (Adult * 189)"/>
            <output expression="&quot;You ordered &quot; &amp; Child &amp; &quot; children and &quot; &amp; Adult &amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>