<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="5255"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:30:42 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzowNjo0MiBQTTsyNTQ0"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzozMDo0MiBQTTs2OzI2NTQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Child, Adult, C, A, total" type="Integer" array="False" size=""/>
            <assign variable="C" expression="120"/>
            <assign variable="A" expression="189"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="C"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="A"/>
            <assign variable="total" expression="(C * 120) + (A * 189)"/>
            <output expression="&quot;You ordered &quot;&amp;C&amp;&quot; children and &quot;&amp;A&amp;&quot; adults &quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp; total &amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>