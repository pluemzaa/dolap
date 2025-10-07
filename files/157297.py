<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="zzz"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:37:35 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzoxMzowOCBQTTsyNTQ0"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzoxOToyNSBQTTsxO2NvbXB1dGVyO0NQQ09NOzI1NjgtMDctMTc7MDI6MjA6NDUgUE07NTI1OA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzozNzozNSBQTTs2OzI2NjM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Childin, Adultin" type="Integer" array="False" size=""/>
            <declare name="Total" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="Childin"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="Adultin"/>
            <assign variable="total" expression="(Childin * 120) + (Adultin * 189)"/>
            <output expression="&quot;You ordered &quot; &amp; Childin &amp; &quot; children and &quot; &amp; Adultin &amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price:&quot;&amp;total&amp;&quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>