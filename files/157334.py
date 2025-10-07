<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="tlab4_1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 04:02:24 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzowMzo0NiBQTTsyNTQ1"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswNDowMjoyNCBQTTsxOzI2NDk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Childprice, Adultprice, total, Child, Adult" type="Integer" array="False" size=""/>
            <assign variable="Childprice" expression="120"/>
            <assign variable="Adultprice" expression="189"/>
            <assign variable="total" expression="0"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="Child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="Adult"/>
            <output expression="&quot;You ordered&quot;&amp;Child&amp;&quot;children and&quot;&amp;Adult&amp;&quot;adults&quot;" newline="True"/>
            <assign variable="Child" expression="Child*120"/>
            <assign variable="Adult" expression="Adult*189"/>
            <assign variable="total" expression="Child+Adult"/>
            <output expression="&quot;Total price:&quot;&amp;total&amp;&quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>