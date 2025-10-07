<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flow1"/>
        <attribute name="authors" value="USER"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:54:06 PM"/>
        <attribute name="created" value="VVNFUjtERVNLVE9QLVFRVjk1QTA7MjU2OC0wNy0xNzswMzo0NDo1MCBQTTsyNjY5"/>
        <attribute name="edited" value="VVNFUjtERVNLVE9QLVFRVjk1QTA7MjU2OC0wNy0xNzswMzo1NDowNiBQTTsxOzI3Nzk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="chirldren, adults, total" type="Real" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="chirldren"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adults"/>
            <assign variable="total" expression="(chirldren*120)+(adults*189)"/>
            <output expression="&quot;You ordered &quot;&amp;chirldren&amp; &quot; children and &quot; &amp;adults&amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;total&amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>