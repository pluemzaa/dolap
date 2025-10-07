<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="testflow"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:34:12 PM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLTZPS0QxVTI7MjU2OC0wNy0xNjswNToxMjoxMyBQTTsyNzQ5"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLTZPS0QxVTI7MjU2OC0wNy0xNjswNjozNDoxMiBQTTszOzI4NjM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <declare name="children, adults, total" type="Integer" array="False" size=""/>
            <assign variable="children" expression="120"/>
            <assign variable="adults" expression="189"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="children"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adults"/>
            <assign variable="total" expression="(children*120)+(adults*189)"/>
            <output expression="&quot;You ordered &quot; &amp; children &amp; &quot; children and &quot; &amp; adults &amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>