<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab_101"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:46:25 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMjo1NTo0MiBQTTsyNTQ3"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzo0NjoyNSBQTTszOzI2NTk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="price, child, adult, total, person" type="Integer" array="False" size=""/>
            <assign variable="person" expression="0"/>
            <assign variable="total" expression="0"/>
            <assign variable="child" expression="120"/>
            <assign variable="adult" expression="189"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adult"/>
            <assign variable="total" expression="(Child*120)+(Adult*189)"/>
            <output expression="&quot;You ordered &quot;&amp; child &amp;&quot; children and &quot;&amp; adult &amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp; total&amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>