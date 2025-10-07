<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_3"/>
        <attribute name="authors" value="PC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 09:24:39 PM"/>
        <attribute name="created" value="UEM7REVTS1RPUC03Q0U2R0tEOzI1NjgtMDctMTk7MDk6MDc6NTkgUE07MjUwMQ=="/>
        <attribute name="edited" value="UEM7REVTS1RPUC03Q0U2R0tEOzI1NjgtMDctMTk7MDk6MjQ6MzkgUE07NTsyNjEw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="nn, n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="n"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="nn"/>
            <output expression="n" newline="True"/>
            <while expression="n &lt; nn">
                <output expression="(n+1)" newline="True"/>
                <assign variable="n" expression="(n+1)"/>
            </while>
        </body>
    </function>
</flowgorithm>