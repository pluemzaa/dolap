<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:55:48 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMjowMjoyNyBQTTsyNTQy"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzo1NTo0OCBQTTsxMTsyNzEx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Price, Child, Adult, Total" type="Real" array="False" size=""/>
            <assign variable="Child" expression="120"/>
            <assign variable="Adult" expression="189"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="Child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="Adult"/>
            <assign variable="total" expression="(Child*120)+(Adult*189)"/>
            <output expression="&quot;You ordered &quot;&amp;Child&amp;&quot; children and &quot;&amp;Adult&amp;&quot;adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp; Total &amp;&quot; baht &quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>