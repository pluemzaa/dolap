<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 04:22:54 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMjo1Njo1MiBQTTsyNTQ5"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswNDoyMjo1NCBQTTs3OzI2NjA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Children, Adults, total" type="Real" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child-120Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult -189Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="Children"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adults"/>
            <assign variable="total" expression="(children * 120)+(adults * 189)"/>
            <output expression="&quot;You ordered &quot;  &amp; children &amp; &quot; children and &quot;  &amp; adults &amp;  &quot; adults &quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht &quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>