<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_1"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 05:35:55 PM"/>
        <attribute name="created" value="QWRtaW47Q0FSTEFSOzI1NjgtMDctMTY7MDU6MjQ6MDEgUE07MjIxNw=="/>
        <attribute name="edited" value="QWRtaW47Q0FSTEFSOzI1NjgtMDctMTY7MDU6MzU6NTUgUE07MzsyMzM4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <declare name="children, adult, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="children"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adult"/>
            <assign variable="total" expression="(children*120) + (adult*189)"/>
            <output expression="&quot;You ordered &quot;&amp;children&amp;&quot; children and &quot; &amp;adult&amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>